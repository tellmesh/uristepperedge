"""uristepper edge CLI — the generic edge command surface (call/explain/routes/
events/flow/serve) is provided by the shared ``uri_control.edge.cli`` builder. Stepper
specifics live in the ``uristepper`` pack (handlers + manifest), not here."""

from __future__ import annotations

import argparse

from uri_control.edge.cli import build_edge_cli

from .runtime import build_runtime as _build_runtime


def _add_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--device-config", default=None, help="Path to device profile JSON")
    parser.add_argument("--events", default=None, help="Path to events JSONL")


def _runtime(args: argparse.Namespace):
    return _build_runtime(args.device_config, args.events)


main = build_edge_cli(
    "uristepper-edge",
    _runtime,
    service="uristepper",
    default_port=8790,
    description="Stepper edge runtime for stepper://",
    add_arguments=_add_arguments,
)


if __name__ == "__main__":
    raise SystemExit(main())
