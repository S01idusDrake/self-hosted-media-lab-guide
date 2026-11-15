# 10. Gluetun and qBittorrent

**Run on:** apps-node. **Requires:** healthy mounted data, Docker, a supported VPN account/configuration and lawful test content. **Produces:** private download UI and verified VPN isolation.

## Prepare the VPN

Read your provider's current Gluetun configuration. The example uses OpenVPN and provider-specific credentials in Compose secret files; WireGuard requires a different reviewed configuration. Choose your provider name, supported region and maintained image digest. Do not assume provider port forwarding is available.

Create the secret files under a private directory using a local editor and restrictive permissions; no values belong in Git. Compose secrets in ordinary standalone Docker are mounted files, not automatically an encrypted secret vault. Protect host files and backups accordingly.

Start **only Gluetun** after private config validation. Check its health and sanitized logs. Record the actual tunnel interface/address and DNS behavior. Do not disable the container firewall to make a failing VPN connect.

## Configure the downloader

1. Start qBittorrent only after Gluetun is healthy. It shares `network_mode: service:gluetun`; publish its UI port on Gluetun only and bind that host port to loopback. Do not attach another normal network to the downloader as a workaround.
2. Reach UI port 8085 through an SSH tunnel. Use the current image's initialization instructions; temporary credentials may appear in private logs. Set a unique administrator password, session/host protections and the actual Web UI port. Never disable authentication to fix proxy access.
3. Set completed downloads under `/data/downloads`, incomplete under `/data/downloads/incomplete`; create movie/TV/music categories matching your managers. Keep category paths on the same filesystem as final media for hardlinks.
4. In advanced network settings, bind transfers to the actual VPN interface (often `tun0` for OpenVPN, but verify). Leave any optional IP binding consistent with provider behavior. UI reachability is separate from peer routing.
5. Use an authorized small test torrent. Verify the observed peer egress through the VPN and absence of traffic on the normal interface using an appropriate test/diagnostic method. Do not treat a browser's public IP as proof of the downloader's route.
6. In an isolated build window, interrupt the VPN using the supported Gluetun method and verify transfer traffic stops, then restore VPN and verify recovery. Coordinate dependencies; do not test by disabling the host's network. Save results. Container health alone is not proof of fail-closed behavior.
7. Set bandwidth, active-download/upload/total limits, ratios and seeding time according to source rules and available storage. Define free-space stop behavior separately from manager import thresholds. Slow queue slots do not automatically replace stalled content; avoid destructive automatic cleanup.

Checkpoint: secured loopback UI, intended VPN IP/interface, working authorized download, fail-closed test and successful recovery. Back up downloader state and VPN secrets encrypted. If the namespace container is recreated, verify/recreate dependents as required; do not leave them attached to a removed namespace.

Source: [Gluetun wiki](https://github.com/qdm12/gluetun-wiki). Use its current provider and health-check pages for version-specific settings.
