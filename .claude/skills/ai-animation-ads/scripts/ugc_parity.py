import subprocess, sys, json, re, statistics as st
import imageio_ffmpeg
from PIL import Image, ImageStat
FF = imageio_ffmpeg.get_ffmpeg_exe()

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stderr

def duration(f):
    out = run([FF, "-i", f])
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    h, mn, s = float(m.group(1)), float(m.group(2)), float(m.group(3))
    return h*3600 + mn*60 + s

def cut_stats(f, dur):
    out = run([FF, "-i", f, "-vf", "select='gt(scene,0.30)',showinfo", "-f", "null", "-"])
    times = [float(x) for x in re.findall(r"pts_time:([\d.]+)", out)]
    cuts = [t for t in times if 0.2 < t < dur-0.2]
    n = len(cuts)
    bounds = [0]+cuts+[dur]
    shots = [b-a for a,b in zip(bounds, bounds[1:])]
    return {"cuts_per_10s": round(n/dur*10,2), "median_shot_s": round(st.median(shots),2), "max_shot_s": round(max(shots),2)}

def speech_density(f, dur):
    out = run([FF, "-i", f, "-af", "silencedetect=n=-32dB:d=0.35", "-f", "null", "-"])
    sil = sum(float(x) for x in re.findall(r"silence_duration: ([\d.]+)", out))
    return round(100*(dur-sil)/dur,1)

def grade_stats(f, dur):
    sat=[]; con=[]; sharp=[]
    for i in range(3):
        t = dur*(0.2+0.3*i)
        subprocess.run([FF,"-loglevel","error","-ss",str(t),"-i",f,"-frames:v","1","-y","_g.png"],capture_output=True)
        im = Image.open("_g.png").convert("RGB").resize((360,640))
        hsv = im.convert("HSV"); s = ImageStat.Stat(hsv.split()[1]).mean[0]
        l = im.convert("L"); c = ImageStat.Stat(l).stddev[0]
        import numpy as np
        a = np.asarray(l, dtype=float)
        lap = abs(4*a[1:-1,1:-1]-a[:-2,1:-1]-a[2:,1:-1]-a[1:-1,:-2]-a[1:-1,2:]).mean()
        sat.append(s); con.append(c); sharp.append(lap)
    return {"saturation": round(st.mean(sat),1), "contrast_std": round(st.mean(con),1), "texture": round(st.mean(sharp),2)}

def utterance_stats(lines):
    counts = [len(l.split()) for l in lines]
    return {"utterances": len(counts), "mean_words": round(st.mean(counts),1), "median_words": st.median(counts), "max_words": max(counts), "pct_le8": round(100*sum(1 for c in counts if c<=8)/len(counts))}

if __name__ == "__main__":
    videos = json.load(open(sys.argv[1]))
    out = {}
    for name, spec in videos.items():
        f = spec["file"]; d = duration(f)
        row = {"dur_s": round(d,1)}
        row.update(cut_stats(f, d))
        row["speech_pct"] = speech_density(f, d)
        row.update(grade_stats(f, d))
        if spec.get("lines"): row["speech"] = utterance_stats(spec["lines"])
        out[name] = row
    print(json.dumps(out, indent=1))
