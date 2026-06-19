# uristepperedge

Thin HTTP edge for `stepper://` on Raspberry Pi, Docker, or other hosts.

Uses shared transport from `uri_control.edge.http` and capability routes from `uristepper`.

```bash
uristepper-edge serve --host 0.0.0.0 --port 8790 \
  --device-config config/device-profile.json
```

Licensed under Apache-2.0.

## Ekosystem TellMesh

Orchestrator: **[urisys](https://github.com/tellmesh/urisys)** · Mapa: **[MESH.md](https://github.com/tellmesh/urisys/blob/main/docs/MESH.md)** · Model: **[ECOSYSTEM.md](https://github.com/tellmesh/urisys/blob/main/docs/ECOSYSTEM.md)**

| Pole | Wartość |
|------|---------|
| **Warstwa** | Edge CLI |
| **Runtime** | `uri_control.edge` (`uricontrol`) |
| **Pack** | uristepper |
| **Port** | 8791 |

Runtime edge: **`uri_control.edge`** w pakiecie **`uricontrol`** (legacy PyPI `uricore` / `urisysedge` usunięty 2026-06).
Resolver intencji: **`uriresolver`** (`uri_resolver`) + transport w **`uritransport`**; policy gate: **`uriguard`** (`uri_guard`).

<!-- end-ecosystem -->
