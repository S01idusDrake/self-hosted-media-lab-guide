# 13. Music: Lidarr, Ombi, slskd and Soularr

**Run on:** apps-node. **Requires:** stable writable music storage, completed media workflow and rights to any test audio. **Produces:** optional music request/import automation.

## Lidarr and music requests

1. Deploy Lidarr with separate local SSD `/config`, chosen digest, UID/GID, loopback port 8686 and a `/data` bind. Add `/data/media/music` as root; do not scan/import an entire existing music collection without reviewing artist/album matching.
2. Set quality/metadata profiles and monitoring preferences. Begin with one artist/album. Connect qBittorrent at gluetun:8085 with category `music`; its completed music downloads must be visible beneath `/data/downloads/music`.
3. Add authorized audio-capable indexers through Prowlarr and test sync. Do not assume every movie/TV source supports music categories or that search success proves seed availability.
4. If music requests are needed, deploy Ombi with private persistent config and loopback port 3579 according to the selected image's documentation. Create a recovery admin, connect Jellyfin and Lidarr with dedicated private API keys, and set normal users to RequestMusic without automatic approval.
5. Test non-admin album request → pending → approval → Lidarr wanted state. Confirm an already-present album is recognized where your versions support it. Only then approve one authorized acquisition and verify import/playback.
6. If Ombi/Jellyfin authentication is incompatible, first check supported versions and upstream fixes. Do not disable authentication or add a header-translating proxy casually. A compatibility shim must be isolated, narrowly scoped, tested and separately reviewed. This edition intentionally does not ship a historical site-specific shim.

## Optional Soulseek path

slskd can provide a separate authorized download source; Soularr connects Lidarr's wanted list to slskd. This is optional and depends on matching, peer availability and project versions.

1. Read upstream image, configuration and API instructions. Create your own Soulseek account and private slskd API credential. Start slskd on an internal network or shared VPN namespace; do not publish its UI/admin API by default. If sharing Gluetun, use `gluetun` as the hostname and its actual slskd port rather than a separate container IP.
2. Persist slskd state in its documented application directory and Soularr configuration in its documented data directory. Mount only the download paths each helper needs, with completed/incomplete paths translated consistently to Lidarr's `/data` view. Configure shares explicitly; do not accidentally share a whole personal library.
3. Configure Soularr with private Lidarr/slskd endpoints and keys, file/quality preferences, batch size and retry interval using its current schema. Avoid inventing extra INI settings from another runner. Start with a small wanted set and reviewed resource limits.
4. Choose a storage floor and stop/alert behavior before automation. Confirm that waiting for a peer is different from a dead process. Use slskd's actual HTTP health endpoint and a meaningful worker heartbeat for automation; no custom heartbeat implementation is included in this draft.
5. Test one authorized album. Inspect track count, album/artist identity, quality, missing tracks, import path and Jellyfin playback. Successful search/download alone does not prove correct matching.

Checkpoint: full authorized sample workflow and resource/storage behavior accepted. Back up config/secrets and transfer state consistently; do not repeatedly copy regenerable search/share caches. Preserve monitored choices on rollback; stop only optional helpers if retiring them. Generic custom retry/storage guards remain open implementation work.

Sources: [Lidarr image](https://docs.linuxserver.io/images/docker-lidarr/), [Ombi image](https://docs.linuxserver.io/images/docker-ombi/), [slskd](https://github.com/slskd/slskd), [Soularr](https://github.com/mrusse/soularr).
