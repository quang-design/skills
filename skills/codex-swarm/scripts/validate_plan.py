#!/usr/bin/env python3
"""Validate a codex-swarm plan JSON file."""

import json
import sys
from pathlib import Path

REQUIRED_LANE_FIELDS = {
    "id",
    "title",
    "model",
    "workflow_path",
    "owns",
    "depends_on",
    "expected_output",
    "proofs",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_plan.py <plan.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1
    errors: list[str] = []

    if not data.get("objective"):
        errors.append("missing objective")
    if data.get("approved") is not True:
        errors.append("approved must be true before execution")

    lanes = data.get("lanes")
    if not isinstance(lanes, list) or not lanes:
        errors.append("lanes must be a non-empty list")
        lanes = []

    lane_ids = set()
    for index, lane in enumerate(lanes):
        if not isinstance(lane, dict):
            errors.append(f"lane {index} must be an object")
            continue
        missing = sorted(REQUIRED_LANE_FIELDS - lane.keys())
        if missing:
            errors.append(f"lane {index} missing fields: {', '.join(missing)}")
        lane_id = lane.get("id")
        if lane_id in lane_ids:
            errors.append(f"duplicate lane id: {lane_id}")
        if lane_id:
            lane_ids.add(lane_id)
        if not lane.get("owns"):
            errors.append(f"lane {lane_id or index} must declare ownership")
        if not lane.get("expected_output"):
            errors.append(f"lane {lane_id or index} must declare expected_output")

    for lane in lanes:
        if not isinstance(lane, dict):
            continue
        lane_id = lane.get("id", "<unknown>")
        for dep in lane.get("depends_on", []):
            if dep not in lane_ids:
                errors.append(f"lane {lane_id} depends on unknown lane {dep}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(lanes)} lane(s) ready for execution")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
