# Example files

Copy examples into a new **private** deployment directory before editing. Do not deploy from this tutorial repository or commit real values here. None of these files is an approved live definition. There is no tested image-version lock in this draft.

| File | Purpose |
| --- | --- |
| `.env.example` | Mandatory image/path/identity/provider worksheet; contains no secret values |
| `media.compose.yaml` | Prowlarr/Radarr/Sonarr/Lidarr/Ombi/Seerr plus optional Gluetun/qBittorrent |
| `prometheus.yml.example` | Host scrape and blackbox relabel skeleton, not complete monitoring deployment |
| `alerts.yml.example` | Simple target/probe alerts; no notification credentials |

## Media example preparation

1. Install Docker/Compose on the intended staging host. Copy `media.compose.yaml` and `.env.example` to your private `/opt/media-lab` directory, renaming the latter to `.env`.
2. Select maintained images from official upstream instructions. Set each `*_IMAGE` to a reviewed immutable reference where available. Fill timezone, intended numeric UID/GID, local config root and verified media mount root. Do not use an existing private installation's IDs/paths.
3. Create required **local SSD** config subdirectories for all selected apps with correct ownership. The example intentionally refuses to create missing bind directories. Create its separate Gluetun directory with permissions appropriate for that image.
4. For the VPN path choose a supported OpenVPN provider configuration and create `secrets/openvpn_user` and `secrets/openvpn_password` privately. Protect them; Docker Compose file secrets do not encrypt the host filesystem. Add any provider-required server/region settings according to current documentation; do not assume the generic skeleton is sufficient for every provider.
5. Run `docker compose --env-file .env -f media.compose.yaml config --quiet` privately. Do not share expanded configuration. Start only the app you are setting up, with `up -d SERVICE`; dependents start only after their prerequisites are valid.
6. The downloader/VPN use profile `downloads`. Explicit targeting may enable a service even without selecting the profile, so review the command. Do not run a blanket `up` before storage and app initialization are accepted.

## Important constraints

All UIs bind to loopback. These examples do not create DNS, proxy, firewall, external ingress, media mounts, authentication, health metrics or backup schedules. Configure those in their chapters. Configuration databases stay local; `/data` maps the verified media root. Directory existence and `create_host_path: false` do not detect a missing mounted filesystem.

LinuxServer app probes assume curl is included; Seerr assumes wget; Gluetun retains its supplied image health check. A chosen release without the tool/endpoint needs a tested replacement, not a disabled check. Health does not prove end-to-end behavior.

Prometheus/alert examples use `<PLACEHOLDER>` target strings deliberately. They need a separately installed exporter, version-compatible validation, datasource labels and an actual private notification route. Never deploy placeholder DNS names or relax TLS to make a probe pass.
