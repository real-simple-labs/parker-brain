# Context Engineering Sync — V2 Architecture

**Date:** May 19, 2026
**Attendees:** Jimmy Slagle, Hannah Houg, Alex Cooper

---

**00:00:00 — Jimmy Slagle:** And let me actually quick do this just so we don't have anything. Okay. So, I mean really like like starting it off — our method of context engineering um is dead. Like it was built for the one-shot era of like, hey, you need to just give AI everything within the context window that it has, provide as much of a harness as possible like here's the steps that you need to take. Um, our context docs didn't really work well with other tools. So it's not like you could easily within the context doc say "hey, go and look at this competitor ad library, find an ad that you like, come back" — like do all of that.

**00:00:40 — Jimmy Slagle:** So it wasn't very agentic. Um, versus what we're — the format that we're moving to is much more like cohesive with context docs and tools as well as uh like kind of what the industry is moving to is like the lower the context window the better the outputs are going to be. Um, and then finally, it's just going to be scalable. Like you can just ask so much more and there's going to be way more ability to make tweaks. Like it's not going to be a whole revamp — like trying to update the versions that we have is not easy. It's very complex. This will make it so um that problem is solved as well. So this is kind of like what the skills era is going to look like. This is not technically like from Claude or any anything else. This is what I have thought of that I think is going to be our best format. So in terms of like what a skill is, which I'll get into a definition later, but really it's composed of four different elements.

**00:01:43 — Jimmy Slagle:** You have the skill document which is like the high-level overview of what is going to uh or the task that you're going to be doing. You have the strategy which is essentially going to be what we are working on, Hannah, with the reasoning agent of determining which is the best way to achieve this task. You have the processes which are all the different ways that you could accomplish that specific task. And then you have the components which — components are just kind of like the tools that the tool calls. Uh, so that's like — tool calls are really for any of the data extraction like if you needed Parker to go and look at X, you know, competitor or organic TikTok or customer reviews, like that's where the tool calls come in. We also have the context docs in general, which are just like, you know, uh the context docs on the brand and um uh like more awareness level. So think um like what Andromeda is, the different types of video formats that exist, different types of static formats that exist, um you know, what Yapper ads are, if you will — those aren't necessarily their own skills.

**00:02:56 — Jimmy Slagle:** They're just knowledge docs that Parker has that if needed,

**Hannah Houg:** Right.

**Jimmy Slagle:** he can he can pull um and reference in his outputs.

**Hannah Houg:** Mhm.

**Jimmy Slagle:** So that's kind of how skills are composed. Uh I will walk through each of these in more detail. So a skill is like just a set of instructions on how Parker should handle a specific task. Um very much so again emphasis on high level. It's it's uh not like how we have it. The way that we have it is more of a process um that you can go to solve a task. The skill is going to be transitioning to like, hey, you know, first you're going to be getting this information — uh, you know, you're going to be getting the brand profile one pager, you're going to be getting the competitor profile one pagers, um you are then tasked to figure out what the best process for this brand is uh to accomplish this task using the strategy doc, then you are going to execute this the the process doc that you choose, and then this is how should output the response to the user.

**00:04:07 — Jimmy Slagle:** So then that would then trigger the strategy doc to be like okay you know this is the best format or process I should say that we should follow and then the process is like the actual execution of it. Um so strategy again it's deciding which is the best process to take based on all the giving context about that brand in general. Again, Hannah, like this is where like what our work on the reasoning layer will directly impact is the strategy. So, as you are coming up with ad ideas, as you're coming up with hooks, as you're coming up with scripts, iterations, it's getting that process of knowing what is the right option um or process to take. uh that that is how Parker like we will make Parker smarter um is through the strategy document itself. One quick note, you're going to see a lot of like MD or like backslashes. Uh MD is really just a markdown file. So it's just straight text file. Backslashes is the folder system that we're going to be rolling into.

**00:05:14 — Jimmy Slagle:** So if you see a backslash, really that just means there's going to be a bunch of sub options below that. So it's not like it's a process doc,

**Hannah Houg:** right?

**Jimmy Slagle:** it's a process folder that contains individual documents. So just as you see that um that's a a quick definition.

**Hannah Houg:** Yeah.

**Jimmy Slagle:** Um processes again are the specific ways that you can accomplish said skill. So if skill if the skill is a script writing skill, these are going to be all the different ways that you in theory can go about creating um a script. Now again, we're not trying to put creative strategy within a box um because that's, you know, not necessarily possible, but I do think there are a lot of ways — if like you really sit down to think about it on how you can come up with an idea to then go and write a script. I think a lot of if we just stay on the script writing uh example, a lot of them are going to end the same with adapting some sort of piece of content at least right away.

**00:06:15 — Jimmy Slagle:** um and not having it be like a straight up like random uh attempt to try to write a really good script. Like I think Parker in this case is going to need some sort of uh uh adaptation, whether that be their own video, um inspo from competitors, inspo from organic, just something along those lines. But how you get to that point — uh I think we can — we'll have a lot of flexibility with this is where a meat of where like your guys's thought process and approaches is going to come in because uh I don't know the right way to go about this because there's just so many levels deep that we could go for creating processes. Um, I'll list some of the ones at the end, but uh, scripting is also going to be the most complex one here. Like iterations, I think, is going to be a great example of this skill where there's maybe, you know, 10 to 15 different iterations that you could make. And you would have a process for each of those different iterations. and Parker, the reasoning doc would be here's how to figure out which of these best, you know, processes is right for this ad.

**00:07:30 — Jimmy Slagle:** Um, so then it's not like one full context doc on here's everything about iterations, all the different types, how to go about choosing. It's like each one has its own process on how to execute it well. And the reasoning doc is helping Parker to figure out which one of those is right for that specific ad. So that's kind of how like the skill the the the strategy and the process work together. And again, if there's like any other information that is needed to to uh execute this idea, whether that be a context doc, whether that be a tool call, like you're able to have that as well. So, within the within the um either the process or just at the very end, uh like you can have it be something where it's like, by the way, these are the context docs that you're going to need to best, you know, uh create this output. and you can just kind of list those as as components. Um, any questions on on kind of the the definitions of these things first?

**00:08:41 — Jimmy Slagle:** Feeling good? Cool. Okay. Um, so this is like an example uh of what this could look like. Like let's just say that we're going to be making a meal for our friend. that is the the skill uh that we are going to be essentially like using. So the skill again high-level document. So this would be what this skill would look like. You'd have a goal like we need to choose and make the best meal possible for a friend. This is how the skill works. You're going to load in the context around the friend. Uh what food we have. Uh recent meals that we've made or the friend has eaten. So that's kind of like the first thing. The second thing is you're going to run the strategy doc to determine the best recipe uh from the different list of you know processes in this case. Um state the pick and the reasoning to our friend is going to be step three. Load the selected recipe and execute that exact process that is listed and then plate and serve the output uh format below which is you know specified right here.

**00:09:48 — Jimmy Slagle:** So this would be an example of like the skill.md file. Uh again, you want to keep this as high level as possible. You don't want it to be like first do this, then do this, then do this, then do this, as like our context docs are. It's like very loose like here's the context that you're probably going to need to execute on this. Or I mean you could even make this even broader of like look through the context docs that you think are most relevant for this exact situation. um uh run the strategy doc. So you're trying to keep that very very high level. Um and then again here would be the components if you needed any. In this case I made it a little more like creative strategy focused just so you could understand um what that could be. But the tool calls — we also will need to work with the engineers just to get those down to where you guys clearly know what all them are so you know and feel confident of like when a tool call would be used.

**00:10:42 — Jimmy Slagle:** But anyways so that's the skill. The skill then triggers the strategy doc which is like okay here's how we're going to pick the best recipe for our friend. So number one, what we're optimizing for — you know, a meal that delights this friend given what they've eaten recently what's available and what they're in the mood for. Uh what to read and what each tells you. So this is the friend profile doc that we have. So any dietary restrictions, allergies, current mood, recent express interest, all of that gets pulled in. what we have available to even make and then again recent meals here. This is like this will change but right away we can have this be something like how to think about each recipe. In our case if we take script writing — how to think about each process to create a script — but then you just kind of like list the the in this case the recipe best for worst for when to use this when not to use this. Um all those sorts of things could be added here.

**00:11:40 — Jimmy Slagle:** uh repeat for the other, you know, recipes. And then even if you wanted to have something that's like guidance on how to pick the best one, uh we could have that be the doc. So Parker would first read this to understand everything. He'd read the friend profile, the pantry inventory, recent meals, have all of that loaded up, as well as like the here's how to select the best one, and then it would choose the process to follow. So, in this case, strategy chooses shrimp pasta. Um, and then this is like the literal recipe to create shrimp pasta that, you know, you would follow to execute it. Well, this isn't anything crazy. If you've ever, you know, cooked anything in your life, it's just exactly what to do. Um, the output then becomes this, you know, "Hey, I'm excited to be making dinner for you. I've decided to make shrimp pasta. I decided to choose this recipe because I know that you love shrimp and it's something you haven't had in a while. You prefer lighter meals, so I decided to go with zucchini noodles instead of traditional ones."

**00:12:43 — Jimmy Slagle:** I, you know, so on and so forth. So, it's just explaining what it did and why. Um, uh, and just like trying to have it be tailored. So, that's like what the user would in essence see along with obviously the meal that is then presented to them. Um, but all of this happens in uh, kind of the background. Um, the last thing in terms of strategy, Hannah, and I guess Alex, what I think this will look like post us having the uh reasoning layer done is more so this being instead of it like "here's how to think through uh each recipe," we would essentially change it to "here's the past picks that we made and why we made them." uh uh like what was our decision process and reasoning that went into each of the different in this case like meals. Um, and that way we're letting AI really use all of this as its context to then be able to see like, okay, why are they doing certain things? And over time, our bet is that Parker would be able to pick up on a lot of your approach, your reasoning, your justification to then be able to like execute this on his own.

**00:14:02 — Alex Cooper:** Could you re-explain this uh

**Jimmy Slagle:** Yeah,

**Alex Cooper:** section

**Jimmy Slagle:** the strategy or just like the uh example once the reasoning layer is live —

**Alex Cooper:** uh like how the example fits into this?

**Jimmy Slagle:** like right here like the —

**Alex Cooper:** Yeah, I'm not not fully following — like I I got it up to uh up

**Jimmy Slagle:** password

**Alex Cooper:** to process, but then when you start talking about the example, I lost

**Jimmy Slagle:** Um, so this is just like — this is post reasoning layer.

**Alex Cooper:** you.

**Jimmy Slagle:** So instead of us just listing out like here are all the ways that you could come up with a script. Um, what we would be giving Parker, maybe it's in addition. Um, it would be here's how we have decided in the past to come up with a script idea and why we decided to come up with that the way that we did. So that way if we just have like a solid, you know, two, three paragraphs on this was the script and this is everything that went into the decision-making process.

**00:15:11 — Jimmy Slagle:** If Parker had say 30 to 40 examples of that, um, our bet is that that context would enable Parker to be able to see how all of these past ideas were executed and therefore be able to um, pick up on the patterns or just decision-making that went into the other ones and be able to create or follow a similar reasoning path uh, for all the others.

**Alex Cooper:** How is that different to memory?

**Jimmy Slagle:** So memory is is much more going to be like personal preferences and ideas that they have liked and uh you know kind of key principles.

**Hannah Houg:** Like is this like keeping track of all the

**Alex Cooper:** It's

**Jimmy Slagle:** What was that?

**Hannah Houg:** changes it's made pretty

**Jimmy Slagle:** So this would be like in in this case,

**Hannah Houg:** much?

**Jimmy Slagle:** you know, it'd be every uh like meal that was picked for your friend and why it was picked for your friend. And if you have done that say 30, 40, 50 arbitrary number times, our bet is that AI is smart enough to be able to pick up on

**00:16:24 — Alex Cooper:** Yeah.

**Jimmy Slagle:** the patterns that exist within all of those decision-making processes um to then be able to choose the right meal for your friend way more consistently than if those did not exist because that's that's —

**Hannah Houg:** How does that how does that like — is that something

**Jimmy Slagle:** Go for it.

**Hannah Houg:** we do or is that just something it keeps track like

**Jimmy Slagle:** Yeah. So, so I mean there's kind of two parts to this.

**Hannah Houg:** Oh,

**Jimmy Slagle:** There's the very specific brand version. So handle like when we roll this out with Salt,

**Alex Cooper:** Oops.

**Jimmy Slagle:** these will be literal examples of you going through and writing the script and why you wrote the script that you did and like your reasoning behind why you think this is good and like all the context that went into it. Um,

**Hannah Houg:** heat.

**Jimmy Slagle:** the goal is for us to be able to get enough of those over time to where Parker can not only just pick up on like what works for Salt, what works for this friend, but if you went and did this for, you know, 15, 20 other people, um, you would essentially get it to the point where it's, uh, like good enough at being able to adapt to —

**00:17:41 — Alex Cooper:** This is not so this is not the the user like the user's like path.

**Jimmy Slagle:** No.

**Alex Cooper:** Okay. Okay. Got it.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** But it's based off of salt or

**Jimmy Slagle:** For like when we're just testing out if like this works. Um yeah, we'll be we'll be taking everything that you do, Hannah, from like a — like when you're actually creating the briefs and the ideas like we'll have all of these

**Alex Cooper:** Yeah.

**Jimmy Slagle:** entries documented.

**Hannah Houg:** And so it's just a test for salt because obviously like that would change per client. So then — I are you saying like we'd have to get like reasoning

**Jimmy Slagle:** Correct.

**Hannah Houg:** for every single industry then?

**Jimmy Slagle:** Uh potentially. I mean, it's it's uh there's ways that we could do it that are more

**Hannah Houg:** 30 to 40 scripts per

**Jimmy Slagle:** optimal. Yeah, there's ways that are more optimal.

**Hannah Houg:** industry.

**Jimmy Slagle:** It just we we would need it to be with brands that you are hyper familiar with because Hannah like part of why we wanted you to do Salt is so we could see what it's like starting from absolute scratch because like there's so much baked in context that you have as a creative strategist for brands that you work with that intuitively if you didn't go with someone that like you'd never worked with before.

**00:19:02 — Jimmy Slagle:** We wouldn't have been able to uncover how deep you need to do research. uh to feel confident to come up with with like good ad ideas.

**Hannah Houg:** Mhm.

**Jimmy Slagle:** So with the other brands where you already have all the existing knowledge that you would need to be able to start to confidently write scripts for so say all of your clients. Um there are ways that we can do this that are much more efficient than uh uh what we are doing with salt.

**Alex Cooper:** Are you

**Hannah Houg:** I definitely just don't want to be the only person.

**Alex Cooper:** concerned?

**Hannah Houg:** Like I I can't I can't do 30 to 40 scripts per industry and like and I don't think it's smart to train the model that way like

**Jimmy Slagle:** Yeah.

**Hannah Houg:** without um because I'm just looking at this I'm like this is

**Alex Cooper:** to do that.

**Hannah Houg:** insane.

**Jimmy Slagle:** Yeah.

**Alex Cooper:** Are you concerned that if the if the the output is going to be there for like this task 30 to 40 times, but the you know say say that it's 30 different brands, but you're not going to have the context in there for the 30 different brands.

**00:20:17 — Alex Cooper:** So like you'll say "here's a decision here's why salt" but like in this output in this like section we're not — it doesn't fully understand salt because salt is one of 30 different businesses in that section

**Jimmy Slagle:** So that — correct. So that is that is essentially what we had to do with Salt to be able to create these which are going to be the new like brand persona context docs.

**Hannah Houg:** What have I

**Jimmy Slagle:** and the competitor uh context docs.

**Hannah Houg:** done?

**Jimmy Slagle:** So essentially what we like our belief is that if we can get the context docs for the brand and the competitor to be essentially as good as what Hannah is doing through this entire process just using AI. So every time a brand signs up, we try to replicate as much of Hannah's process of learning as possible. If we can get all of that context established then we are betting that it just comes down to okay when you have all that context what do you actually do with it and why and that's where the the reasoning layer becomes more streamlined because we don't have to go through all of this again like Parker we can assume that the context is is an even playing field for what a creative strategist would —

**00:21:39 — Hannah Houg:** outside of what the user gives you in terms of memory,

**Alex Cooper:** Peace.

**Hannah Houg:** brand context, stuff like that that they're

**Jimmy Slagle:** And yeah,

**Hannah Houg:** updating.

**Jimmy Slagle:** and how we can even get this to be better is — again like Andrej Karpathy,

**Hannah Houg:** Yes. Yes.

**Jimmy Slagle:** did you see he joined Anthropic which is

**Hannah Houg:** Crazy.

**Jimmy Slagle:** nuts.

**Hannah Houg:** It's actually crazy. I did see that.

**Jimmy Slagle:** But anyways, he came out with this auto research. So I think like what we're going to be able to do to try to get it to be good enough at multiple different brands is this kind of reinforcement learning loop which is you know you run a task using a skill. So assuming all the context the new context is live say —

**Hannah Houg:** Yeah, my my husband sent up something like this for me um in my on my Claude based

**Alex Cooper:** No

**Jimmy Slagle:** for

**Hannah Houg:** off of like my process turned it into a skill and then has it doing constant um like a feedback loop auto research like this.

**00:22:28 — Alex Cooper:** heat.

**Jimmy Slagle:** yeah yeah — so so essentially we assuming that all the context

**Hannah Houg:** So that's crazy.

**Jimmy Slagle:** is there Parker would then say it's script writing uh in this case — would run — we'd have Parker run the script writing skill for the perfect gene — someone that like we haven't done the technically research layer on, but I think at least Alex, you probably know well enough to be able to deduct whether the reasoning is sound or not sound. So, Parker runs the skill. Um, we get the overview of like the what what process was chosen or you know just the whole end-to-end uh kind of thought chain of what Parker was doing and how he came to the script that was generated. Alex or Hannah, you know, whoever, you just have to know the brand well enough to be able to provide this this type of feedback. would give feedback to Parker saying, "Hey, you know, technically that's not a good idea because there was only 12 customer reviews and it really wasn't a —

**Hannah Houg:** tell Parker now. Like there's no way to like tell him something's

**00:23:27 — Jimmy Slagle:** valid.

**Alex Cooper:** Yeah. Yeah. Yeah. This is so this is — this is where the reason layer — I mean we're doing the reason layer current is interesting but like this is where it

**Hannah Houg:** bad.

**Alex Cooper:** gets really interesting because then I think you just go and hire like every every top

**Jimmy Slagle:** Yeah.

**Alex Cooper:** strategist and get them to bring one of their clients in and just go through

**Jimmy Slagle:** Yep.

**Hannah Houg:** Yes,

**Jimmy Slagle:** Exactly. Yep. Yeah. And we can go through it for each of

**Alex Cooper:** this

**Hannah Houg:** that's I see. So then the foundation's been set. They don't need they already have their context.

**Jimmy Slagle:** the

**Hannah Houg:** We're able to make that happen on our Parker side because of my original reasoning layer. And then from there it's just training it on what good, bad,

**Alex Cooper:** Yeah, that's that's the game. Like I I saw a tweet from uh Taylor Holiday.

**Hannah Houg:** reason.

**Alex Cooper:** I don't know if it was like um uh I don't know if it if he was like overemphasizing being uh serious, but like he said he spends most of his day just in auto research feedback loops just like role-playing uh different situations and giving feedback to the LM.

**00:24:30 — Hannah Houg:** I was

**Alex Cooper:** um as like that that is the that is the world we're heading to and the more people that we have going through that loop the

**Jimmy Slagle:** Yep.

**Alex Cooper:** the more the concept of

**Jimmy Slagle:** Exactly. And the more variety of brands that we have,

**Alex Cooper:** compound

**Jimmy Slagle:** the more that this gets better and better and the strategy doc just is better and

**Hannah Houg:** Okay, question. But what about — Okay, what what is the threshold for script writing?

**Jimmy Slagle:** better.

**Hannah Houg:** Like as we — we just talked like 30 to 40 brands or 30 to 40 scripts per industry whatever — let's just say like — does that need to happen first before the auto research how — because that's like the overall script scripting reasoning because obviously I'm

**Jimmy Slagle:** Yeah.

**Hannah Houg:** just one one person one brain script writing and that would they for would people that come in first write scripts themselves

**Jimmy Slagle:** Honestly,

**Hannah Houg:** or

**Jimmy Slagle:** they could just go straight to the auto research side of things, assuming that they knew the brand.

**00:25:36 — Jimmy Slagle:** Well, Alex, this is also where brand tags.

**Hannah Houg:** just don't trust my reason. I would not only bank on my reasoning

**Jimmy Slagle:** No, no, no, you're good. So, so like honestly Hannah Urus is going to be very fine-tuned for

**Hannah Houg:** like

**Jimmy Slagle:** salt and like everything from the onboarding process. There's a world in which because like this is going to update the skill.

**Hannah Houg:** Right.

**Jimmy Slagle:** Um what we can do with the what with what like we have done with with you

**Hannah Houg:** Right.

**Jimmy Slagle:** is like — I mean that could be an enterprise sort of uh addition where like we document all the

**Alex Cooper:** Good.

**Jimmy Slagle:** reasoning and have that like as examples as you saw it. um um within that that con like the second kind of version. But in a perfect world, we would have it to where uh this skill is again being modified and updated based on if we have six people that are helping us out, if we have 10, like I don't know exactly what it is, but again, they would see a script that's generated

**00:26:37 — Hannah Houg:** I'm baseline. I'm the baseline. But then it only it will reasoning because of

**Jimmy Slagle:** Yeah, more more than anything I think like where again it's going to be — Salt's going to be OP because they're going to

**Hannah Houg:** that.

**Jimmy Slagle:** have like everything custom made for them. Uh uh and like all this extremely fine-tuned. But as we try to make this skill universal,

**Alex Cooper:** Thank you.

**Jimmy Slagle:** that's where we're just going to need more people providing feedback on on like brands that they're very confident in. And then that skill, so the one script writing skill is global for everyone. The strategy document is really what's probably being updated based on like here's how to determine what you should do. And this is, you know, everything that you need to be aware of and like how script writing in general works and different edge cases across different uh uh uh like categories. There's also a world in which like we have sub-skills that are skills for different industries or different — like we don't know where it's going to go but this is probably going to be the — um this is probably going to be the best way for us to at least start and learn uh what works well and what doesn't.

**00:27:56 — Alex Cooper:** So to to clarify, will there be anyone like — are we — is it someone — is the next person going to come in and go straight to auto research or is there going to be someone else on the ground level like so it's not just Hannah's

**Jimmy Slagle:** Yeah.

**Alex Cooper:** process?

**Hannah Houg:** Like I wouldn't bank on just mine.

**Jimmy Slagle:** So, no, no, no. You're good.

**Hannah Houg:** I'm telling you all the competitor all that stuff is

**Jimmy Slagle:** It It won't just be yours. Uh

**Hannah Houg:** fine. I think that's pretty industry standard but up to

**Jimmy Slagle:** Yeah, again like where where we are going to need more people if you will

**Hannah Houg:** script.

**Jimmy Slagle:** are are the processes um because that is that is what's going to be technically different every time and again like I don't know exactly what the right format of how we approach processes are — like is it starting with a persona — is it starting with a gap that of like a white space of a persona. Is it starting with an ad format?

**00:28:59 — Jimmy Slagle:** Uh, and kind of following like what Alex had scoped out with like the create tab of like you select the ad format you like, you know, so on and so forth, but like that just turning into a skill. Um, is it starting with the creative diversity audit and seeing like, okay, you know, what gaps exist in our creative strategy? um and what should we be prioritizing to where then it picks a persona and then based on that persona it picks an ad format and based on that ad format it finds you know inspo from competitors affinity whoever as like a baseline of like here are five examples of ways that they've done it make it your own to this brand now uh like I don't know exactly what that flow of like the specific process is going to be all I know is for script writing we're going to need a lot of —

**Hannah Houg:** Mhm.

**Jimmy Slagle:** Um because there's again just so many ways. Yeah.

**Hannah Houg:** Right.

**Jimmy Slagle:** So so then the reasoning is like how do you pick that one?

**00:29:59 — Jimmy Slagle:** Um but if we only have five examples of processes then we're — that's also a limitation because there's you know more processes than just that. Um, so that's where ideally it's like auto research kind of goes first to be like here's the the overview and what I found. Ideally the creative strategist could be like oh actually you know it should be you start with the persona but then you actually go directly to the creative diversity audit to figure out you know what format you haven't tested and then you you go and do X Y and Z. So it's like they're equally like creating new processes as they're fine tuning the skill

**Hannah Houg:** And then so if we're supposed to tell it like what process to go through,

**Jimmy Slagle:** itself.

**Hannah Houg:** like how will it know? Because obviously you said you want to leave it like vague enough for AI to like be able to learn and just like know, but like how do we not confuse it at the same time? have like 10 different people saying this is how they're process.

**00:30:56 — Jimmy Slagle:** Okay.

**Hannah Houg:** No, I wouldn't do it that way, but Alex would do it a completely

**Jimmy Slagle:** Yeah. I mean, again, I think it's all uh like we'll we'll figure out those fine details of like overlapping.

**Hannah Houg:** different

**Jimmy Slagle:** Vague is really just the skill. The strategy document, we actually want it to be pretty specific in terms of like how to think about the right idea or process um to go down. And like that's where we can make this one a pretty advanced document in terms of like how to choose the right process to execute on based on the brand. Um, so that one is where we can have it be a decently meaty uh document, but that's also where we could have sub-documents too. Like we could have a strategy doc for again health and wellness brands or

**Hannah Houg:** Mhm.

**Jimmy Slagle:** luxury brands or uh problem solution brands or you know whatever. Like that's where that's where like this could become a a very uh in-depth web uh over time. Um if we think like that is where yeah like the level of detail that we need to go.

**00:32:16 — Jimmy Slagle:** So does that help make a little more sense?

**Hannah Houg:** Yes.

**Jimmy Slagle:** Cool.

**Hannah Houg:** From a very high level.

**Jimmy Slagle:** Cool.

**Alex Cooper:** Yes.

**Jimmy Slagle:** Because I mean there's also a world in which each brand could have their own strategy document kind of like what we talked

**Hannah Houg:** Yes.

**Jimmy Slagle:** about like that's what Salt's going to have is like Salt Strategy because all of this is just going to be custom to what Hannah has done so far. Um so there's a world in which that could exist for for every brand too. Um we would just need someone to like go through the process of fine-tuning it.

**Alex Cooper:** Yeah. Or Hannah could just go and do the research process for every customer when they come on

**Jimmy Slagle:** I you know I was thinking about that but I wanted you to say it

**Hannah Houg:** Why not?

**Alex Cooper:** board.

**Jimmy Slagle:** first.

**Hannah Houg:** Every every single Parker customer. Why not?

**Jimmy Slagle:** Yeah.

**Hannah Houg:** Every single one.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** And we can start with the agencies.

**00:33:08 — Alex Cooper:** Charge charge extra 50 bucks a month.

**Jimmy Slagle:** Yeah. 50 I that might be a little

**Hannah Houg:** Thank you guys.

**Jimmy Slagle:** steep.

**Hannah Houg:** So kind. So kind.

**Jimmy Slagle:** Okay. So if we give like a literal creative strategy example now. So user query is you know "write me a script." The first thing that happens uh just so you're aware again like Parker is going to determine like okay do I need do I need a plan to execute this or a skill to execute this or am I fine without using it. So if this were to actually

**Hannah Houg:** strategy example. So like sorry I guess I did have one question and maybe you'll answer it later but just like

**Jimmy Slagle:** Yeah.

**Hannah Houg:** where like our original thinking around like starting from format starting from messaging and then using the AI tagging bases like it's like initial starting point — is that still in this process conversation um just an example right just like an

**Jimmy Slagle:** Yep.

**Hannah Houg:** example

**Jimmy Slagle:** Yeah.

**00:34:12 — Jimmy Slagle:** Totally. So that's where like within the skill itself, it won't be as rigid as like — like you only can follow this and there's no

**Hannah Houg:** Oh,

**Jimmy Slagle:** other steps. Really, we're just trying to like — in these examples, I'm just trying to solve for like the generic "write me a script."

**Alex Cooper:** Yes.

**Jimmy Slagle:** If they were to say, "Write me a script for Bigger Guys," or something along those lines, when it gets to the actual process of where I'm sure there'd be a step somewhere uh along the lines of like having a persona in mind,

**Alex Cooper:** Yeah.

**Jimmy Slagle:** it would just factor that the user input uh into that specific part. um still follow the other.

**Hannah Houg:** create write me a POV ad. Would it going through this whole process or would it just be taking its

**Jimmy Slagle:** Yeah.

**Hannah Houg:** best best like bet at a POV ad that already exists and then with the brand context

**Jimmy Slagle:** Technically, it would it would go through the process of writing a script.

**Hannah Houg:** like

**Jimmy Slagle:** Now, if you gave it more context, if you said, "Write me a POV ad like this," where you pasted in a um uh you know, like a — Yeah. It would then just pull probably the adapting scripts uh skill if you know,

**00:35:23 — Jimmy Slagle:** we had that be its own

**Hannah Houg:** Interesting.

**Jimmy Slagle:** skill.

**Hannah Houg:** My brain's having a hard time figuring out how those are working together, but it might become

**Jimmy Slagle:** Yeah. Yeah. I mean, again,

**Hannah Houg:** clear.

**Jimmy Slagle:** it's going to be an ongoing thing that we'll we'll figure out as long as we don't just put a harness on it enough. Uh, like AI is smart enough to be able to pick up on those things. Our existing context docs are just like very strong harness like this is what you need to do. So, as long as we just loosen the reins on that, um,

**Hannah Houg:** Yeah.

**Jimmy Slagle:** like AI's good enough to to know like it won't just discard what the user gave you. Um, so yeah. Anyways,

**Hannah Houg:** Oops.

**Jimmy Slagle:** so in this case, it's going to determine like yes, I need a skill uh to execute this uh user query. So the first thing that is going to happen is pull in its memory. So this is the brand profile.

**00:36:18 — Jimmy Slagle:** This is the brand notes from the org, which I'll show some of these later. Uh the user profile, the user notes from the org. Um going to determine if a skill is needed, if yes, what Parker does.

**Alex Cooper:** Yeah.

**Jimmy Slagle:** So this is called the YAML — it's called the YAML front matter. uh kind of a technical term, but all Parker is going to see in terms of what skill it should use is the skill name and like a two sentence description of that skill and when it should be called. Um, so this way if we have 50 different skills that are accessible, the context window actually isn't that bloated because it's not that much text um in the grand scheme of things. So this is where we can just add a lot of skills because uh the context won't get bloated and Parker will still be able to have a good output. Um so you can see like again script writing — an example of the YAML front matter — script writing this skill explains how to create scripts — for use this use this when someone wants a script generated — something along those lines.

**00:37:21 — Jimmy Slagle:** We could make it a little more complex and nuance if we really needed, but again AI is pretty smart to be able to determine uh the intent behind users and if this would be the right skill. In this case, obviously it would be. So Parker would select the skill uh the script writing skill. Um this is kind of how the file system works. So it's the same thing of like you know Parker just seeing all the skill names and descriptions as like the different processes. So when the reasoning doc is called, we don't pull in every single process of how to do it and all the different steps. It's just the name of the process and a description for what that process is and when it's best used. Something along those lines. So that way again,

**Alex Cooper:** Yeah.

**Jimmy Slagle:** Parker isn't going to be bloated on context. It's just going to see the name and the description of the process, and that's what is going to be used to determine if it is the right fit.

**00:38:16 — Alex Cooper:** Yes.

**Jimmy Slagle:** Now again, AI is smart. It's not just going to go and say, "Oh, I think this is the one." And then if it reads it and then is like, "Oh, that's maybe not a good one." Like AI is good enough to be able to be like, "Oh, I'm going to go and check this one out." "No, I actually don't think that is right for this case. I'm going to go and check this one out." So, it's able to at least like — like it's again, it's not just it has to one-shot it. Like, it can think and reason through the best one. Um but it again just limits the amount of context that gets ingested. Um and then same thing with references like you have the knowledge docs, you have the tool calls uh for the specific skill. Um so that's just kind of the high level overview. If we look at the actual skill file, this is what again an example could look like for um script writing in general.

**00:39:08 — Jimmy Slagle:** So we could have it start with the brand context um parse user uh provided constraints from the request. So Hannah, this is what you're talking about. Uh so we could have it essentially have an understanding of what the user is already given and how

**Alex Cooper:** Hello.

**Hannah Houg:** Factor that

**Jimmy Slagle:** to yeah how to factor that in — decide whether to run the

**Alex Cooper:** Yeah.

**Hannah Houg:** in.

**Jimmy Slagle:** strategy or not. That's the other thing is like technically if if they already have everything given to you. Yeah. Like it doesn't need to. if running strategy um you know pick the right process for the brand's current uh state factoring in any constraints output the reasoning chain to the user before running anything. So we could even have that like we could essentially have there be a human in the loop here where Parker would give the overview of "Hey, this is the uh you know persona I'm going to be going after" or in this case like "here's what you provided me, here's the strategy that I think is going to be best for salt based on these different factors and these contexts what do you think" and then it could just be like a no or yes

**00:40:06 — Alex Cooper:** That's

**Jimmy Slagle:** um and you know then there's at least like a human to to agree or not — then you know load depict process and run it format output per uh the required output structure which is

**Alex Cooper:** two.

**Jimmy Slagle:** defined below. So this could be the you know output structure that we want. Um but you know strategy runs by default only skip in these specific situations. Iterations on a prior run.

**Alex Cooper:** This

**Jimmy Slagle:** So if you're just like going back and forth like there's already a script written um above like

**Alex Cooper:** one

**Jimmy Slagle:** you wouldn't have to go through it to make a slight change every single time. Um and then yeah so on and so forth. So like we can add some some high-level again harnesses to to each of the different skills at the skill MD level. Um but then this would be you know in this case a strategy doc.

**Alex Cooper:** This

**Jimmy Slagle:** So here we'd be defining the different context docs that are most important to be able to determine which process is best.

**00:41:05 — Jimmy Slagle:** We could tell Parker to read through them to get a good understanding of the brand. Here's how to think through each process. you know, adapt competitor ad uh best for,

**Alex Cooper:** is

**Jimmy Slagle:** worst for. This is not, you know, a lot of time like don't take this as like this is what we're going to do. This is just the example of like what this document could look like, not literally the processes that we would be um implementing. Uh adapting organic TikTok, best for you know this, worst for this. Start with an ad framework,

**Alex Cooper:** This

**Jimmy Slagle:** best when this, worst for this, so on and so forth.

**Alex Cooper:** work.

**Jimmy Slagle:** So like that's kind of what the strategy doc could in essence look like or the structure of it. Uh Parker would then determine which one of these would be best and then it would go through

**Alex Cooper:** Yes.

**Jimmy Slagle:** and that process would have a specific uh uh process

**Alex Cooper:** Thank

**Jimmy Slagle:** to follow. So in this case starting with a persona — you know this is what — this when this process gets

**00:41:52 — Alex Cooper:** you.

**Jimmy Slagle:** picked it's observed an underserved persona um that we should be targeting and creating an ad for — here's the required inputs — here's what you need to get from the tools — here's what you need to get from you know any sort of like reference docs or the knowledge docs or the brand contacts uh from the user as well — um and then step by step this is how you're going to execute it using the start with persona. Look through the customer reviews for that persona. Find how they talk. Identify three to five, you know, recurring words or phrases that you're seeing. Look across the global ads database for, you know, ads that have targeted this persona. Uh so on and so forth.

**Alex Cooper:** Where?

**Jimmy Slagle:** So like that's the level of granularity that we could go and take all of these different processes um to best execute it. And then finally, this is like the output. So here's the script that it would generate. how we decided on this script uh validation plan that we did and yeah so on and so forth — any like this is kind of just the agenda of — or the the appendix of like here's everything I found and why

**00:43:12 — Alex Cooper:** Uh, can you explain how this fits — like how this like slots into proactive — cuz like that's obviously the big thing around this is V2,

**Hannah Houg:** Let's

**Alex Cooper:** but also like we're redesigning the app for it to be proactive first. Like how would this fit into

**Hannah Houg:** chat

**Jimmy Slagle:** Yeah,

**Hannah Houg:** first.

**Alex Cooper:** that?

**Jimmy Slagle:** I mean the goal is is like technically we would just have you know the proactive run be run this skill um to let the user

**Hannah Houg:** come up with concepts and then say which scripts like they want to execute on or something

**Jimmy Slagle:** Yeah.

**Hannah Houg:** from that

**Jimmy Slagle:** Yeah. I mean like again uh if it's script writing it could just be like "run the script writing skill to

**Hannah Houg:** or

**Jimmy Slagle:** determine five scripts that this brand should be using." Um if it's something around like customer reviews I mean we could have a skill that's an how to analyze customer reviews well.

**Alex Cooper:** Yes.

**Jimmy Slagle:** Um not every skill — Yeah.

**Hannah Houg:** I'm super

**Jimmy Slagle:** Yeah.

**00:44:10 — Jimmy Slagle:** Not every skill needs like a ton of processes either.

**Hannah Houg:** excited.

**Jimmy Slagle:** Um, like that's the fortunate thing is again script writing is just the beast that is going to exist of so many different ways. But like analyzing customer reviews really could be five and it's looking for objections, looking for uh uh like golden nuggets of words or metaphors that are used. Um, it could be looking at common response —

**Hannah Houg:** Or it could also be taking your — okay say like you save down ideas throughout the week then it can look at that week write the scripts and come to you Monday morning with your ideas fully fleshed. like ready to go for you pretty much from the last

**Jimmy Slagle:** Yeah. Yeah. We'll get into like how ideas will fit into this,

**Hannah Houg:** week

**Jimmy Slagle:** but um the TLDR,

**Alex Cooper:** Yeah.

**Jimmy Slagle:** Alex, is it really shouldn't change anything. If if anything, it should just make it better. Um because we won't need to worry about like prompting as

**Hannah Houg:** rely on user input as much.

**00:45:16 — Jimmy Slagle:** much.

**Alex Cooper:** What?

**Hannah Houg:** It should be able to actually do the job with

**Jimmy Slagle:** Yeah.

**Hannah Houg:** them.

**Jimmy Slagle:** And if and if you don't want a skill because like technically analyzing the ad account could be a skill um of just like here's how to analyze the ad account and we just take the existing context doc and turn it more into like a skill format um which I think we'll be able to do for a lot of them

**Hannah Houg:** Yeah.

**Jimmy Slagle:** that we already have is just like this is the overview of what we're doing and our new skill

**Hannah Houg:** Yeah.

**Jimmy Slagle:** process. um uh like take this doc and turn it into this new new version. Um so yeah, and and not every doc is going to need like a strategy document either. Like again, that's really just for the ones where there are a lot of different ways to do something that are so nuanced and and like context dependent and brand uh dependent. But like analyzing an ad account, you know, you you probably could just have that be the skill doc and maybe again like two or three different processes if

**00:46:21 — Alex Cooper:** Yeah.

**Jimmy Slagle:** anything.

**Alex Cooper:** Okay. Okay. So, what does this look like to execute on? Because there's a lot

**Jimmy Slagle:** Good question. Yeah, good question. So,

**Alex Cooper:** of

**Jimmy Slagle:** the first and foremost thing is we're going to have to go through and start to create these different skills. Uh so how like what I'm trying to do to make this as easy as possible for us is again we kind of have the four parts that make up a skill. Um, and the fun part about all of these skills is we essentially just get to assume like, okay, if this is the format that we needed in, these are all the context docs and tools and knowledge docs available to us that we could then create the different processes

**Hannah Houg:** current that currently

**Jimmy Slagle:** around. Yeah.

**Hannah Houg:** stand

**Alex Cooper:** Do we have a list anywhere of everything we need to All

**Jimmy Slagle:** uh that is what I'm working on within this document which is like

**Alex Cooper:** right.

**00:47:21 — Jimmy Slagle:** Parker V2 and we will have the like context engineering tasks um that are due for all of this. what I want you guys cuz like I can focus on a lot of like the prompts like generating the competitor one pager, the brand one pager based on like what Hannah and I have done. Again, what we need and that's where like this is kind of what this next phase because I don't know exactly what this is going to look like. We're just going to need to start creating the skills and within the skills creating all of the different uh strategy documents and within there creating all of the different processes for each of the different skills. I would say do script writing, you know, maybe not first. Um do like iterations or something along those lines uh first because I think that one would be like a really good one for us to just feel confident around. Um, but that's that's kind of like it's going to be a lot. This is um in terms of the priorities. Number one,

**00:48:20 — Hannah Houg:** H

**Jimmy Slagle:** we just need to also finalize the context docs that we want because I think it's going to be easiest if it's almost viewed as like an allocart thing. So when you're coming up with the right process, you know,

**Hannah Houg:** we use assign numbers so that I can keep track of like — because there's going to be so many like if we're going to go do this process like I think every concept context doc needs like an ID if that makes

**Alex Cooper:** Uh yeah.

**Jimmy Slagle:** Yeah.

**Alex Cooper:** Well, yeah, I think we need to list. Go on, Jimmy.

**Hannah Houg:** sense.

**Alex Cooper:** Go go go

**Jimmy Slagle:** Yeah. So like number one,

**Alex Cooper:** then.

**Jimmy Slagle:** we just need to finalize the context docs that we want uh to be a part of like what we can choose from. So everything here is technically what I have come up with,

**Hannah Houg:** Mhm.

**Jimmy Slagle:** but this is not an exhaustive list. Like if there's something that we are missing here that you guys are like, "Oh yeah, we definitely need this." Or even on the knowledge docs,

**00:49:12 — Jimmy Slagle:** like I mean there's there's probably a lot that we uh can add here. Um

**Hannah Houg:** a Yapper ad is an ad format. Just gonna let every know that.

**Jimmy Slagle:** yeah. Yeah. Yeah. Yeah. No,

**Hannah Houg:** I'm so tired of Parker getting me

**Jimmy Slagle:** that's — Yeah, you're good.

**Hannah Houg:** out.

**Jimmy Slagle:** And I mean, yeah, technically we could have a doc around each of the different formats if we

**Hannah Houg:** I think you have to.

**Jimmy Slagle:** wanted.

**Hannah Houg:** I think you absolutely have

**Jimmy Slagle:** So, so there's just a lot of probably knowledge docs that we also will need created to like best be able to do creative

**Hannah Houg:** to.

**Jimmy Slagle:** strategy. Um, again, we can we can decide what the exact skills are that we want to create. Um, because I don't necessarily know like all them that we're going to want. It's where like I'm just teaching you guys how we can create them and it's going to be a group collective to be like, "Okay, here's everything that we need um in order for for,

**00:50:09 — Alex Cooper:** Okay.

**Jimmy Slagle:** you know, Parker to think and be like a top creative strategist." Um but then it's it's like finalize the context docs, finalize the skills that we want, begin creating all the different processes for each of the different skills. uh probably have a break there. Like that's a big enough task as is.

**Hannah Houg:** No.

**Jimmy Slagle:** I want to then actually have all of the existing context — like the new

**Alex Cooper:** Yes.

**Jimmy Slagle:** contexts that will be generated for brands when they onboard. Um or I mean all the existing ones will get it too. But like all of all of these uh context docs, I want that to be live before we really do anything else just so that when we can actually come and like start to create the scale docs, like we'll be able to test it right away. We don't have to wait for that to be done and like there would be a week or two or something like that. That would slow us down.

**Alex Cooper:** Okay. So help me understand here.

**00:51:17 — Alex Cooper:** So firstly we have to list out all the context docs that the skills are going to pick

**Jimmy Slagle:** this. Yeah,

**Alex Cooper:** from.

**Jimmy Slagle:** I mean the context docs are just like the kind of like the brand context like what I showed you. If there's anything else that like we are missing from like the brand context or

**Alex Cooper:** Sure.

**Hannah Houg:** So that log in and they set up the account.

**Jimmy Slagle:** the — Yeah.

**Alex Cooper:** Okay.

**Hannah Houg:** It can make sure it does that pretty much. Yeah.

**Jimmy Slagle:** So this is all like the foundation.

**Hannah Houg:** All the original

**Alex Cooper:** Then and then pick all the skills.

**Hannah Houg:** context

**Jimmy Slagle:** Yeah.

**Alex Cooper:** So that is like an extension of the knowledge docs like fill that messed up.

**Jimmy Slagle:** Yeah. So again, like the skills are the high-level overview of how to accomplish a task and you're really just guiding it to be like here's the information that you're going to be getting or like how to handle very specific edge cases. So the knowledge docs are going to just be a part of the skill in order to execute the skills correctly.

**00:52:25 — Jimmy Slagle:** So like let's just say script writing — a knowledge doc that could exist within script writing is uh you know video ad

**Alex Cooper:** Please.

**Jimmy Slagle:** formats um and that could be a context doc or knowledge doc that is given which is just here's all the different video ad formats that exist um that you need to be aware of when like coming up with an idea.

**Alex Cooper:** Okay. So,

**Jimmy Slagle:** Um

**Alex Cooper:** so if we were to do that task number two and say list out all the skills, do you think it's better to like — is there a starting point here or should we just start listing these out from a blank

**Jimmy Slagle:** yeah,

**Alex Cooper:** slate?

**Jimmy Slagle:** I mean like we could take some of the ones that we have. We just have to really uh uh differentiate between what is just a knowledge doc — like this is something you need to be aware of — versus like this is how you do something um and execute something because I think that's the

**Hannah Houg:** information how like of actually how to do it but then the skills is just the steps and what is required — the high level that it's going to go execute and what it's going to bring in — all the tools everything like that — and so we okay

**00:53:39 — Jimmy Slagle:** sort of like knowledge doc — again you can think of that as just general information. Um it's less of like Yeah.

**Hannah Houg:** the context doc

**Jimmy Slagle:** Yeah. Yeah. Exactly. Yeah. Just again our like what we have named context docs and how they are created in Parker is combining these two things together. It's saying this is how you do something and this is everything that you need to know about X. What we are switching to is like this is how you do something is becoming the processes and this is everything that you need to know about X is becoming the knowledge doc. So it's like just taking the existing documents that we have — instead of like step one do this, step two do this, step three do that, step four do that. All of that becomes a process. Everything below which is like here's everything you need to know about script writing in this case — like is a knowledge doc itself.

**Alex Cooper:** And then what is the skill version of that?

**Jimmy Slagle:** Um it's it's essentially being able to

**00:54:37 — Alex Cooper:** Like what does skill do?

**Jimmy Slagle:** utilize both of those things.

**Hannah Houg:** how to use those two

**Jimmy Slagle:** Yeah. So, so again,

**Hannah Houg:** things.

**Jimmy Slagle:** like if we go back to the um if we go back to the example, it's like here's the information that you are going to need to know to write a script. So, first like pull in this context. Um second, you know, look through what the users provided you to determine like what new information you're going to need or just like maybe not even new information you need, just like to be aware of. Then decide whether you need to run the strategy doc or not — like is there enough information here to where you probably don't need to run the strategy to pick you know the whole right process. Then if you are running it um uh output like the process that you're going to go with based on you know um what you've seen or what you've learned or the context that you have for the brand. uh load that specific process and execute it and then format the output to the user.

**00:55:44 — Jimmy Slagle:** So this is very much like the high-level overview of

**Alex Cooper:** Okay. So if we're then going to take this to like say people in in the next

**Jimmy Slagle:** it.

**Alex Cooper:** call, would the steps in that call be to brainstorm all of the the the knowledge docs and the the context docs and the

**Jimmy Slagle:** Yeah,

**Alex Cooper:** skills?

**Jimmy Slagle:** honestly honestly you guys you guys will probably start to identify like if again you go all cart — meaning like these are the current docs that you have access to

**Hannah Houg:** and these are actually all docs right now.

**Jimmy Slagle:** that uh at least that I put together like at least correct

**Hannah Houg:** Do you — from our research and stuff you've already put together these contexts?

**Jimmy Slagle:** Yeah. Well,

**Hannah Houg:** Wow.

**Jimmy Slagle:** not — they're not like — this is just the the label of them all.

**Hannah Houg:** Oh,

**Jimmy Slagle:** Like there's no — Yeah,

**Hannah Houg:** so they're

**Jimmy Slagle:** there's no information in these docs,

**Hannah Houg:** not

**Jimmy Slagle:** which is which is why I added this pause at step four, which is like just wait till we have all the existing context docs to like actually go in and like start to write the script or the skill.md file and the strategy file because like it — you won't be able to test it until we have all the foundational context created.

**00:57:04 — Hannah Houg:** And there's not a way to like make those context docs from our conversations or is — is was that the

**Jimmy Slagle:** No. Yeah,

**Hannah Houg:** plan because that would be the context

**Jimmy Slagle:** I mean that's definitely something we can do. Um, uh,

**Hannah Houg:** that's how I would do the thing. So,

**Jimmy Slagle:** yeah.

**Hannah Houg:** obviously for extra ones we haven't put in this list and that doesn't exist. Then we'd need to create those

**Jimmy Slagle:** Yep. Yep. Exactly. Um but anyway,

**Hannah Houg:** too

**Jimmy Slagle:** so again like — like identify which skills we probably need first and then as you're going through the processes I'm sure you will learn like oh Parker doesn't really have knowledge around how to do that well — like selecting a persona uh or ident — like right now like Parker has no

**Hannah Houg:** Right.

**Jimmy Slagle:** real context

**Hannah Houg:** But we're to — and like that is the proc — that is the context. That is it.

**Alex Cooper:** So,

**Hannah Houg:** So,

**Alex Cooper:** is this — is this me and Hannah task or is this is the one you want the whole group to refine?

**00:58:13 — Jimmy Slagle:** Uh I mean there like where the group would probably get most like uh where we get the most value out of the groups is the

**Hannah Houg:** who's the group? Who's the groups?

**Jimmy Slagle:** process — like you're bring on extra context engineers.

**Hannah Houg:** What are we talking about here? Are these just like

**Alex Cooper:** Um, so like Sarah will be in these meetings, Harry will be in these meetings, anyone else who want to pull in. I'm probably going to pull in either Anna or Payton,

**Hannah Houg:** Yeah, need some help.

**Alex Cooper:** probably both of them. Um, and anyone else that we want to riff on these sessions. basically what the AI workshops were for — this is the V2

**Hannah Houg:** I see. I see. Okay.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** And then we would riff on that specific thing as

**Alex Cooper:** version.

**Hannah Houg:** No.

**Jimmy Slagle:** Yeah. Like the goal would be for them to just like help us think of more processes by which you could like do things and and why you would do them like that because that's going to be probably the the meat of a

**00:59:02 — Hannah Houg:** Okay.

**Jimmy Slagle:** lot of these is getting down all the different ways that you in theory could do any of the skills. Um and that's probably where we would get the most value from external people.

**Hannah Houg:** Mhm.

**Alex Cooper:** Okay. So, step one and step two,

**Jimmy Slagle:** Cool.

**Alex Cooper:** Hannah and I will go and do it to start off with. What's step three?

**Hannah Houg:** Awesome work, by the way, Jimmy. This is so cool to see all laid out.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** I can't imagine how much thinking this took to put together. So,

**Jimmy Slagle:** Yeah.

**Hannah Houg:** thank you.

**Jimmy Slagle:** Yeah. You're welcome. So, yeah. finalizing like any other context docs that we need the skills and the processes. Um, wait till we have all the new contexts, foundational contexts for a brand. Then we can actually go and start to like create the skill.md files and

**Hannah Houg:** and we'll likely need help at step three to begin those.

**Jimmy Slagle:** strategy.

**Alex Cooper:** Okay.

**01:00:13 — Hannah Houg:** I just can't foresee us being able to push — Yeah.

**Alex Cooper:** Step three is the beast.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** I can't foresee us being able to like on a timely manner with me doing the research layer too. Like I'm just trying to figure out how this is going to like

**Alex Cooper:** Yeah.

**Hannah Houg:** happen.

**Alex Cooper:** How how long do you think this iteration will take, Jimmy? You know the process better than anyone

**Hannah Houg:** Yeah.

**Jimmy Slagle:** I mean, it all depends.

**Alex Cooper:** else.

**Jimmy Slagle:** Uh, I think there like there's — this is going to be a living document for a long time. uh because I think there's always going to be new variations or permutations of ways that we could execute writing a script. Um, so I mean if we're confident that like starting with an untapped persona and like going through that to come up with a script, starting with a format that could be worth testing, starting with uh uh

**Hannah Houg:** message idea.

**Jimmy Slagle:** like Yeah.

**Hannah Houg:** A key big idea

**Jimmy Slagle:** Yeah.

**01:01:17 — Jimmy Slagle:** Something along those lines. 70% of the way there. I don't think it'll be that long. I think obviously like it's just that's not going to be — uh we we'll probably hit some sort of like people saying it feels like it's the same thing. So the more breath that we can have the better, but I think there is going to be like an 80/20 here of where if we can get the core um processes down uh it will allow us to have better outputs.

**Alex Cooper:** Um, Yeah. And then what does it look like from like what do we need to do on the M side to actually make this possible to build and who's responsible for

**Jimmy Slagle:** Yep. So, yep. So,

**Alex Cooper:** that?

**Jimmy Slagle:** I've been meeting with Manish and Tanner. This whole thing, which is essentially based on the uh uh Excalidraw that you just saw. This is all based on like the engineering tasks that are needed and the context engineering tasks that are needed. I think we're going to have Anton and Roshan working on all the different kind of phases to um to this — my goal though like in a perfect world because again there's there's so many uh architectural prompts that I'm going to need to work on to be able to generate like all the

**01:02:37 — Alex Cooper:** Where's

**Jimmy Slagle:** information and how open loops and hypotheses validations and dreaming and all of that's going to — Like in a perfect world, I can hand over a lot of this process to you guys and I can again be like the expert in making sure that the prompts everywhere else are in like a really good spot. And obviously I'll I'll help with this, but the more that I can educate you guys on how this is going to in my head work and me get out of your way to allow you guys to be able to train the next creative strategist or the people that are going to come in and help with our uh process,

**Hannah Houg:** Yeah, I'm

**Jimmy Slagle:** the more efficient that we will be. because again right now um I am just the bottleneck

**Hannah Houg:** back.

**Jimmy Slagle:** on anything like prompt or context uh related for part one V2. So that's where it's like the more that we can just start to um like do these sessions and get you guys fully ramped

**01:03:48 — Alex Cooper:** Okay, Cool.

**Jimmy Slagle:** up

**Alex Cooper:** So, do we actually need to put in the session with other people this week? I don't feel like that's the immediate next

**Hannah Houg:** I don't think so.

**Jimmy Slagle:** No, I don't think we need to. I I again,

**Alex Cooper:** step.

**Jimmy Slagle:** it's just like it's the mo — the most important thing is you guys. And if you guys are going to be comfortable enough to be able to like go and teach other people how to do this, uh then that's great.

**Alex Cooper:** I think once we've done it ourselves, we'll be able to

**Jimmy Slagle:** This this — Yeah, this may also help too. Like this is something I just uh had vibe coded earlier just so you can start to like get a good understanding of how this will work. So in terms of the context docs themselves um this is kind of what the new — and again don't take this as like a visual over — this is solely for the purpose for you guys to be able to see the new like context engineering.

**01:04:45 — Jimmy Slagle:** This is not what the Parker app is going to look like. Um but you can see like so this is my profile. So, I have a profile that Parker will create and update on an ongoing basis on who I am, uh, how I want to work with Parker, what he expects from outputs, how I give feedback, what he cares most about, stuff like this. It'll just be like a narrative of like who I am based on how I use Parker. There's going to be version controls that again are updated every so often. Uh, there's going to be a brand notes from user. So, when I'm working with, in this case, AG1, the notes for that specific brand. So, uh, what I like, what I don't like, you know, whatever. I mean, this isn't like a literal example of what this doc could look like, but you'll at least get the picture. Brands. So, this is like the AG1 brand profile. Um, these would be all the sub-context that like would be, you know, these ones that would be here.

**01:05:39 — Jimmy Slagle:** Uh, running notes. So, brand notes from the org. If there are seven people that are using uh Parker from AG1, you'd essentially be able to see like this is how the team is using Parker and what value they're finding and so on and so forth. Um we could have the personas, so all the different persona profiles that are created based on this. We can have the open loops be something that's here. We can have the skills. So as you see like this is the script writing — this is the script writing skill MD — when to use the skill — how it's going to work — the inputs — the output format — u you know the different available processes — we could just have the index file — uh this is the strategy doc of like how to think through like what we just talked about um and then all of these different skills that would be there — this would be the knowledge docs so on and so forth — so like this is how the new kind of context system is going to work in general and every file layer that you go deeper — again it's that YAML front matter so Parker's just going to be seeing the name in the description.

**01:06:49 — Jimmy Slagle:** Um, now this is actually something uh, Alex that again like I mean I'm still super bullish on what — based on co-work which uh, we do not need to take as a literal reference but I do like the idea of something in the right hand bar as like the the um, new experience for chat. So trying to figure out what that could look like. One thing that I think is really cool is if we could almost see Parker's reasoning behind everything over on the right hand side. So you'll see it start to work like — part — you you'll essentially be able to read Parker's thought process on how it's coming and making decisions. We can have human in the loop of like if you wanted to step in and like redirect Parker that could be there. But um so this is where you could start to see like the tracing uh based on the chat itself. Parker could have a running board of ideas that's again just like for this chat that the user could

**Alex Cooper:** Yes.

**Jimmy Slagle:** easily like save to the actual ideas tab.

**01:07:52 — Jimmy Slagle:** Um if we wanted memory to be here and then in terms of research like this is the loops hypothesis validation. So if there's anything from the chat that kind of becomes an open loop um it could be stored here and uh kind of go through the whole process. Um, so again,

**Alex Cooper:** here.

**Jimmy Slagle:** not saying that like this is what it has to be, but just, you know, an idea of what it could look like. Um, the other thing that I really like too is we could almost have dreaming be

**Alex Cooper:** Okay.

**Jimmy Slagle:** its own kind of thing that like people could run if they wanted. So this is something where like based on uh recent conversations and like new data from Parker, it like refreshes Parker's uh like knowledge base like the global ads. um if there's new data sources coming from the brand. So you could essentially like start this cycle so it could read through recent conversations,

**Alex Cooper:** Please.

**Jimmy Slagle:** find any new data sources, uh compare against like the memory and persona that it has um and then like recommend like or just show anything that's like new or interesting that could be relevant for the brand too.

**01:08:57 — Jimmy Slagle:** So yeah, but nonetheless, I think this is this is like a way for you to kind of see how this will all be stored as

**Alex Cooper:** Okay, got it.

**Jimmy Slagle:** well.

**Alex Cooper:** Do you want like — I'm thinking out loud here. Do we want to overengineer on UX for the chat if like Parker is not going to be chat first?

**Jimmy Slagle:** Well, again, I don't know if like — like I was saying the other day, I don't know if it's literally like zero chat or full chat. I I do think it's somewhere in the middle. I think it's like how can you just make the chat experience 10 times better is probably a better question that we should solve for versus like what does it look like — or at least maybe um an alternative route that we should explore equally to like what does it look like for Parker to be like entirely not chat first or if the chat experience was 10 times

**Hannah Houg:** Yeah, I don't know if I would use Parker if you took out the chat completely.

**01:10:03 — Jimmy Slagle:** better.

**Alex Cooper:** I'm not saying take out the chat completely. No, no one's suggesting that. I'm saying like in a world where is not chat first.

**Hannah Houg:** Right.

**Jimmy Slagle:** Yeah.

**Alex Cooper:** Like I I think Parker will push ideas to you as the

**Hannah Houg:** Right. Which I agree with you,

**Alex Cooper:** as the primary value prop and then it's like oh if you want to join into an idea you can. If you want to start a completely new chat you can but it's not like what you go

**Hannah Houg:** right? That's the first step. Yeah. Okay.

**Alex Cooper:** to.

**Jimmy Slagle:** Yeah, I mean it it also depends because like I I I was just telling uh Manish and um like the an — there is a world in which I also don't know if our uh from from a quality an internal perspective if Parker can deliver you 10 briefs that are A+ um that are ready to go like — like yeah we we have done something incredible. I don't actually know if that's what the user wants because I I think there is still at least if if we are on the co-pilot for creative strategists um they they want to feel a part of the process of coming up with those and so

**01:11:16 — Hannah Houg:** Yes.

**Jimmy Slagle:** like there is an alternative — a temporary alternative to be um you know how can we make it so a creative strategist would only want to do their work within Parker and that being the primary use case of the app. But then,

**Hannah Houg:** Mhm.

**Jimmy Slagle:** you know, like if we just deliver insights to a small business owner or a company that doesn't care about the creative strategy process, like sure. Um, so that that's one thing that that I have thought of too is like if if Hannah just got 10 ad briefs for a brand without being able to feel a part of that

**Hannah Houg:** Yeah,

**Jimmy Slagle:** process.

**Hannah Houg:** you're actually getting rid of creative strategists that way.

**Jimmy Slagle:** Uh, yes.

**Alex Cooper:** That's

**Jimmy Slagle:** But but it's also just like

**Hannah Houg:** Like from a brand perspective, they would be like, "What?

**Jimmy Slagle:** Yeah.

**Hannah Houg:** Why do I need a creative strategist if Parker is mine?

**Jimmy Slagle:** Yeah. But it it it also just brings up a question of like even if those ideas

**01:12:19 — Alex Cooper:** control,

**Jimmy Slagle:** were — what was that?

**Alex Cooper:** right? Receive

**Jimmy Slagle:** Yeah. And like Hannah would be — everyone is going to be skeptical of what AI just gives you.

**Alex Cooper:** control.

**Jimmy Slagle:** And even if we had a ton of like good reasoning for each of the different ideas, um I do still think there's going to be something to like can we literally just do the process for them but have them click a few buttons to

**Hannah Houg:** Exactly. Like in Claude where you're like, "Do you want it this way or this way?" Bump bum. And then you're like, "I did something.

**Jimmy Slagle:** Yeah, at least again for creative strategists — for all the brands that exist that like literally just cannot afford a creative strategist or uh haven't been able to hire a good one or like again Hannah can only work with so many brands and there's a lot more brands that would need Hannah. Um I think that's a different profile uh

**Alex Cooper:** That's good.

**Jimmy Slagle:** or persona or the use case around what the web app is like.

**01:13:15 — Jimmy Slagle:** So that's the one — that's the one thing that I have been thinking about

**Alex Cooper:** Yeah.

**Jimmy Slagle:** which again it would be a really fun experiment, Alex, for you if you were to just sit down and dream and say what would the perfect chat experience look like as a creative strategist? that would be,

**Alex Cooper:** Good.

**Jimmy Slagle:** you know, dream scenario. Uh, like throw out anything that you think is possible. Like what would that experience even look like? Um, or maybe it's not even a chat. Like, I don't know. But like if if Parker was the only thing that you that you use for creative

**Alex Cooper:** It's difficult because I — it I might give

**Jimmy Slagle:** strategy

**Alex Cooper:** a different answer for me versus like if it was someone else's tool. Because I like for me — Hannah it's the it's the — what did you say D call it — the ice box was it — it's that — it's that spreadsheet — the ideas library that

**Hannah Houg:** Oh yeah. Yeah. Yeah. Like your ice box.

**01:14:27 — Alex Cooper:** I've showed you before Jimmy — it's it's literally the ideas database of pre-populated ideas that Parker has gone and done all the strategy work and I can just click approve or reject — that's for me

**Hannah Houg:** Thank

**Alex Cooper:** but yeah yeah but that's assuming that you trust the platform — if it's someone else's platform that I don't know how the mechanic work and I can't like unless I

**Hannah Houg:** That's

**Alex Cooper:** really trusted the reasoning I would be — or felt like I had some — this is where it's different

**Hannah Houg:** true.

**Alex Cooper:** maybe — if you had some input — like if I trained that model — if I if I like was going through the process of of uh the auto research process of going like I like this I don't like this then I would feel like I could trust the ideas that get pre-populated because I felt like I had got an idea in it but if it's like someone else

**Hannah Houg:** you.

**Alex Cooper:** has gone and you mean effectively what Parker is today — Parker is the culmination of like us giving it

**Hannah Houg:** That's true.

**01:15:18 — Alex Cooper:** processes, but like for someone coming in, there's no like I don't know what the thinking is behind this.

**Hannah Houg:** Even

**Alex Cooper:** I wouldn't I wouldn't trust I yeah I would trust I wouldn't trust UX like that because I I

**Hannah Houg:** good ideas. You might not trust it.

**Alex Cooper:** wouldn't feel had a part of it but if I'd helped train that even if like even just someone saying like yes I no I don't and here's why then I for me the and for I think quite a lot of strategists would be the ideas database populated

**Jimmy Slagle:** Yeah. Yeah. Yeah, I mean

**Hannah Houg:** And then being able to click a button and have it the script literally be

**Jimmy Slagle:** just

**Alex Cooper:** a button. If I want to drill down into idea, if I want to chat to an idea,

**Hannah Houg:** made.

**Alex Cooper:** then I can to ask it like, "Oh, why'd you come up with this?" or like, "Can we adjust this?" or um — that would be my dream process for it to come out and I just press approve or like push to production and goes and makes the ad.

**01:16:14 — Hannah Houg:** I would like it if it came to me with the script and then something similar to Claude. It was a side by side where I was able to like make any last minute changes myself and then hit like

**Alex Cooper:** You wouldn't want like idea first and then script. So you want the script straight

**Hannah Houg:** no, I'd still want idea.

**Alex Cooper:** away.

**Hannah Houg:** Say yes, I want to go with this one. Um, or it would come to me weekly or whenever my sprint schedule is and then it drops it drops the concepts based off of the last week

**Alex Cooper:** Yeah.

**Hannah Houg:** or the last month, whatever that cadence be that's in the ice box. Um, it flushes them out further. It says here's what I've got for you and here's like my reasoning behind each one and where I would

**Alex Cooper:** Yeah.

**Hannah Houg:** prioritize. And then I would say like great, approved, approved. Let's go build out these scripts. So then it would go build out the scripts and then I would be like pinged or something.

**01:17:07 — Hannah Houg:** When the scripts are done, I go in and I can like review and if I want to make changes, it would show up on a side by side like Claude. So I know I can see the script. It's like I'm editing it. Um, and then boom, I can export directly from there, but also I have the way that I brief.

**Alex Cooper:** Yeah.

**Hannah Houg:** That's another important thing is like how you yourself brief because every brand is different. And so I would want it in a perfect world to export to my brief structure with all the information — who the target persona is, what the goal of the messaging is, and be ready to go to a creator or whatever the end executed result would

**Alex Cooper:** Yeah.

**Hannah Houg:** be.

**Alex Cooper:** But yeah, I mean like notice how neither of those two experiences are like chat first. Um which to be fair,

**Hannah Houg:** Yeah.

**Alex Cooper:** this is exactly what we told um Eugene last week and like you know he mocked — I don't know if you saw it in the channel, but he mocked up something today that like was too similar to what you know the rest of the

**01:18:07 — Hannah Houg:** I was like, it looks

**Alex Cooper:** app. Did you see it?

**Hannah Houg:** different.

**Alex Cooper:** Oh, you saw it in the design. Yeah. I was like, Eugene, like we told you to go make something different. Um, structurally though, you know, I do like the idea of that kind of page where it's like here's opportunities. Here are like what I

**Hannah Houg:** It'd be so cool to have a dashboard almost of like full dashboard that I get to log

**Alex Cooper:** found.

**Hannah Houg:** into and like here's like — I don't know — it could give me like stats on my previous — it could like give me high-level and then it's like coming up this week or this sprint here's what we've got like want me to approve want me to script write any of these — a dashboard of like everything in one place

**Alex Cooper:** Yeah.

**Hannah Houg:** would be

**Alex Cooper:** Yeah. I mean,

**Hannah Houg:** incredible.

**Alex Cooper:** regardless, like doesn't change anything about this this process, but yeah, UI is something that all has to uh work through.

**01:18:57 — Alex Cooper:** I don't know. They had a meeting today.

**Hannah Houg:** Yep.

**Alex Cooper:** I don't know what like how that went down as the transcript, but yeah, it should be able to be done if we go and do the backend work. Yeah.

**Hannah Houg:** Yep.

**Alex Cooper:** Well, that would be a dream if if you could get like a a the database that comes up with ideas every week and I can train it and say if I reject an idea, it says why don't you like this? And I can see it getting better over time. Um that would be a dream.

**Hannah Houg:** And that's that's the user input right there.

**Jimmy Slagle:** Yeah.

**Hannah Houg:** It can be even just like how good are the ideas, you know, uh that are presented. So,

**Alex Cooper:** Yeah. Yeah.

**Hannah Houg:** Yep.

**Alex Cooper:** What would you rate this — like one to 10 and and why? I don't know. Um how could it be better? Anyway, I have to I have to run. My food is probably cold.

**01:19:48 — Jimmy Slagle:** Yeah.

**Alex Cooper:** I have to sprint downstairs um and get that. But is there anything else we need to go through, Jimmy?

**Jimmy Slagle:** No,

**Hannah Houg:** Okay.

**Jimmy Slagle:** that's — how are you guys feeling just in terms of like clarity on uh this new

**Alex Cooper:** Good, good.

**Jimmy Slagle:** format?

**Alex Cooper:** Yeah, Hannah, I'm going to message you if you've got time this week. We can get in a call and start

**Hannah Houg:** Yeah, I'll probably have time for one more call.

**Alex Cooper:** banging.

**Hannah Houg:** Um I uh yeah, my biggest question is just how it's like actually going to be executed and like making sure we have the right help to make sure that we can move quickly um on it because that's my biggest constraint is just like I really only have like outside of the reasoning layer like four hours to work with. So I'm just like how is that gonna happen? Um, so however we can like work on that part would be awesome because I do want this to be like a sprint towards that as well.

**Alex Cooper:** Yeah, we will have to first work out everything that's needed and then we can work out how much we need

**Hannah Houg:** Yeah. So, let's do that and then um yeah,

**Alex Cooper:** to.

**Hannah Houg:** just message me. We can put some time in.

**Jimmy Slagle:** Do you guys have draw too?

**Alex Cooper:** No,

**Hannah Houg:** Any what?

**Alex Cooper:** could you send that? I mean he said

**Jimmy Slagle:** Yeah.

**Alex Cooper:** anyway

**Hannah Houg:** Have what?

**Jimmy Slagle:** The uh presentation. Yeah.

**Alex Cooper:** I

**Hannah Houg:** Oh yeah, please send that over with this call recording too, maybe.

**Alex Cooper:** um — All right guys I have to run. I'll message you Hannah.

**Hannah Houg:** Okay, sounds good.

**Alex Cooper:** Okay thank

**Hannah Houg:** Thank you so much, Jimmy. This was awesome.

**Jimmy Slagle:** Yeah.

**Alex Cooper:** you.

**Jimmy Slagle:** All right. Going to see you guys.

**Hannah Houg:** Talk soon.

**Transcription ended after 01:21:29**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*
