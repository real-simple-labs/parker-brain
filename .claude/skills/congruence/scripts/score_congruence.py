#!/usr/bin/env python3
"""Calculate the fixed-weight Parker Congruence score."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping


WEIGHTS = {
    "ad_message_person": 0.20,
    "audience_delivery": 0.30,
    "ad_page": 0.25,
    "delivery_page": 0.25,
}


def calculate_congruence(scores: Mapping[str, float]) -> dict[str, object]:
    missing = [name for name in WEIGHTS if name not in scores]
    if missing:
        raise ValueError(f"Missing score(s): {', '.join(missing)}")

    normalized: dict[str, float] = {}
    for name in WEIGHTS:
        value = float(scores[name])
        if not 1.0 <= value <= 10.0:
            raise ValueError(f"{name} must be between 1 and 10; got {value:g}")
        normalized[name] = value

    contributions = {
        name: round(normalized[name] * weight, 3)
        for name, weight in WEIGHTS.items()
    }
    weighted_losses = {
        name: round(weight * (10.0 - normalized[name]), 3)
        for name, weight in WEIGHTS.items()
    }
    overall = round(sum(contributions.values()), 1)
    largest_leak = max(weighted_losses, key=weighted_losses.__getitem__)
    mockup_trigger_seams = [
        name
        for name in ("ad_page", "delivery_page")
        if normalized[name] <= 6.0
    ]

    return {
        "scores": normalized,
        "weights": WEIGHTS,
        "weighted_contributions": contributions,
        "overall": overall,
        "weighted_losses": weighted_losses,
        "largest_leak": largest_leak,
        "landing_page_mockup_required": bool(mockup_trigger_seams),
        "mockup_trigger_seams": mockup_trigger_seams,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate a 1-to-10 Congruence score from four required seams."
    )
    parser.add_argument("--ad-message-person", required=True, type=float)
    parser.add_argument("--audience-delivery", required=True, type=float)
    parser.add_argument("--ad-page", required=True, type=float)
    parser.add_argument("--delivery-page", required=True, type=float)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scores = {
        "ad_message_person": args.ad_message_person,
        "audience_delivery": args.audience_delivery,
        "ad_page": args.ad_page,
        "delivery_page": args.delivery_page,
    }
    try:
        result = calculate_congruence(scores)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
