from __future__ import annotations

import json
import os
from pathlib import Path

from uri_control.edge.runtime import compose
from uri_control.edge.runtime import Runtime


def load_json(path: str | os.PathLike[str]) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build_runtime(device_profile_path: str | None = None, events_path: str | None = None) -> Runtime:
    profile_path = device_profile_path or os.environ.get("URISYS_DEVICE_PROFILE") or "config/device-profile.json"
    profile = load_json(profile_path) if profile_path and Path(profile_path).exists() else {}
    events = events_path or os.environ.get("URISYS_EVENTS_PATH", "data/events.jsonl")
    return compose.build_runtime(
        packs=["uristepper"],
        config={"device_profile": profile},
        events_path=events,
    )
