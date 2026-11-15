# 11. Sonarr, Radarr, Prowlarr and optional FlareSolverr

**Run on:** apps-node UI over SSH tunnels. **Requires:** accepted chapter 10 and common `/data` mapping. **Produces:** a controlled import workflow, not a bulk library migration.

## Bring up managers

Start Prowlarr, Radarr and Sonarr individually using reviewed images and local SSD `/config` directories. Bind host UIs to loopback. Set image-supported UID/GID/umask so media writers share access; do not pass those settings to images that do not support them. Confirm local `/ping` health responses and secured admin login. Each app needs its own config directory.

In Radarr add `/data/media/movies`; in Sonarr add `/data/media/tv`. If you want Kids/Anime roots, create corresponding directories and libraries first, then add them explicitly. A manager root is a destination, not permission to rename/move all existing files.

1. Add qBittorrent download clients at `gluetun:8085` when on the same Docker network. Use a dedicated app credential if supported, and categories `movies` and `tv`. Test the connection. Do not use the host's localhost inside the manager container.
2. Enable hardlink imports where supported. Use identical download path visibility in client/manager. Avoid remote path mappings unless you actually need translation; they do not fix permissions or cross-filesystem links.
3. Enable completed-download handling. Choose whether automatic upgrades/deletions are allowed before adding monitored content. Keep unattended upgrades conservative while learning.
4. Configure quality profiles and preferred sizes by testing candidate results. If targeting H.264 clients, use supported custom-format rules and scores for AVC labels and reject incompatible labels, but inspect the actual imported codec afterward. Release names can be wrong; audio/subtitles/bit depth also affect direct play.
5. Set a free-space import reserve suitable for your OS/data volumes. It is not a reserved partition and does not stop the downloader automatically. Add a separate storage guard/alert.

## Configure indexers and sync

In Prowlarr, add only sources you are authorized to use. Prefer maintained native Torznab/Newznab definitions where available. Store any keys in private settings. Configure Sonarr/Radarr application endpoints and API keys; test each then sync. Select sync scope intentionally so Prowlarr does not overwrite app-specific choices unexpectedly.

If indexer traffic should use the VPN, configure Gluetun's internal HTTP proxy per its current documentation and enable it only on selected/tagged indexers. Keep proxy/control ports internal. Verify a request takes the intended route. Metadata APIs and normal manager traffic may still use the standard host connection.

FlareSolverr is an optional browser helper for supported sources, not a universal fix for blocked sites. Use its maintained image, an internal endpoint (commonly port 8191), resource limits, a matching proxy tag and a lightweight HTTP health check. Do not expose it publicly or assume every challenge/provider is compatible. Skip it if no selected source needs it.

## Controlled acceptance

Add one authorized movie/episode with an explicit root/profile; first inspect manual search results, then approve one download. Verify completion, import path, file permissions, device/inode/link count where relevant, actual codec and Jellyfin playback. Check that a rejected or pending request does not start downloads. Avoid bulk missing searches/imports at initial setup.

Rollback: disable the specific integration/indexer or monitoring flag, preserve queue/data and restore only selected settings from your private baseline. Do not roll back a whole database over current requests just to remove one source.

Source: [Servarr Docker paths and permissions](https://wiki.servarr.com/docker-guide); [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr). Application UI details must be checked against your selected release.
