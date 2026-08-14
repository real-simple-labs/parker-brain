#!/usr/bin/env python3
"""Regression checks for the Congruence skill's fixed score contract."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORER = ROOT / ".claude/skills/congruence/scripts/score_congruence.py"


def load_scorer():
    spec = importlib.util.spec_from_file_location("score_congruence", SCORER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCORER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CongruenceScoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scorer = load_scorer()

    def test_perfect_path_scores_ten(self) -> None:
        result = self.scorer.calculate_congruence(
            {
                "ad_message_person": 10,
                "audience_delivery": 10,
                "ad_page": 10,
                "delivery_page": 10,
            }
        )
        self.assertEqual(result["overall"], 10.0)
        self.assertFalse(result["landing_page_mockup_required"])

    def test_fixed_weights_and_largest_leak(self) -> None:
        result = self.scorer.calculate_congruence(
            {
                "ad_message_person": 8,
                "audience_delivery": 6,
                "ad_page": 7,
                "delivery_page": 5,
            }
        )
        self.assertEqual(result["overall"], 6.4)
        self.assertEqual(result["largest_leak"], "delivery_page")
        self.assertTrue(result["landing_page_mockup_required"])
        self.assertEqual(result["mockup_trigger_seams"], ["delivery_page"])

    def test_landing_page_score_of_six_triggers_mockup(self) -> None:
        result = self.scorer.calculate_congruence(
            {
                "ad_message_person": 9,
                "audience_delivery": 9,
                "ad_page": 6,
                "delivery_page": 8,
            }
        )
        self.assertTrue(result["landing_page_mockup_required"])
        self.assertEqual(result["mockup_trigger_seams"], ["ad_page"])

    def test_missing_seam_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Missing score"):
            self.scorer.calculate_congruence(
                {
                    "ad_message_person": 8,
                    "audience_delivery": 6,
                    "ad_page": 7,
                }
            )

    def test_out_of_range_score_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "between 1 and 10"):
            self.scorer.calculate_congruence(
                {
                    "ad_message_person": 11,
                    "audience_delivery": 6,
                    "ad_page": 7,
                    "delivery_page": 5,
                }
            )

    def test_mockup_contract_files_are_shipped(self) -> None:
        skill_root = ROOT / ".claude/skills/congruence"
        build_process = skill_root / "processes/build-landing-page-mockup.md"
        quality_standard = skill_root / "references/mockup-standard.md"
        self.assertTrue(build_process.is_file())
        self.assertTrue(quality_standard.is_file())
        self.assertIn("Never change the live site", (skill_root / "SKILL.md").read_text())
        self.assertIn("375 pixels wide", build_process.read_text())
        self.assertIn("scrollWidth", build_process.read_text())
        self.assertIn("Common AI design tells", quality_standard.read_text())


if __name__ == "__main__":
    unittest.main()
