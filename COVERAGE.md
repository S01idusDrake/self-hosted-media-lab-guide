# Coverage and implementation status

Every identified subsystem has a destination below. **Written** means beginner procedure drafted; it does not mean a clean installation passed. **Example** means a generic configuration exists with mandatory placeholders. **Gap** means a dependency or custom implementation still needs work. The scope comes from reviewed build notes; it is not a guarantee every historical experiment has been rediscovered.

| Subsystem | Chapter | Included / remaining work |
| --- | --- | --- |
| Hardware choice and two host roles | 01–02 | Written; exact hardware compatibility test pending |
| Ubuntu install, updates, Intel Mac/PC branches | 02 | Written; model-specific driver screens pending |
| Gateway, managed router/switch, VLANs, DHCP | 03 | Written vendor-neutral flow; exact device configs intentionally absent |
| Mesh/AP mode and backhaul | 03 | Written; vendor UI variants pending |
| SSH, console, vault/emergency access | 04 | Written + SSH example |
| Physical disks, mount identity, filesystem/ACLs | 05 | Written; filesystem creation requires deliberate target review |
| NFS exports, matching identities, hardlinks | 06 | Written + export/fstab templates; clean two-host test pending |
| Docker Engine, Compose, updates, persistence | 07 | Written + media Compose example |
| AdGuard Home DNS, upstreams, rewrites | 08 | Written; version-specific standalone Compose pending |
| Jellyfin native server, libraries/users/transcoding | 09 | Written; GPU/version matrix pending |
| Playback-reporting/intro-detection plugins | 09 | Optional flow; per-plugin install/version recipes pending |
| Gluetun, VPN provider, HTTP proxy, isolation | 10–11 | Written + OpenVPN example; provider matrix/fail-closed test pending |
| qBittorrent categories, queue/seeding/storage limits | 10 | Written + Compose example |
| Sonarr, Radarr, Prowlarr, indexer sync | 11 | Written + Compose example; no provider list supplied |
| Native Torznab/Newznab sources | 11 | Written integration flow; choose your authorized providers |
| FlareSolverr | 11 | Optional flow; image-specific Compose pending |
| Seerr, approvals and category routing | 12 | Written + Compose example; UI/version acceptance pending |
| Lidarr and Ombi | 13 | Written + Compose example; authentication compatibility testing pending |
| slskd, Soularr, wanted-list/import paths | 13 | Written optional flow; validated generic Compose/config pending |
| Custom music runner/retry/storage guard | 13 | Gap: design requirements only; not ported as tested software |
| Music/Jellyfin auth-header bridge | 13 | Gap: prefer upstream compatibility; no generic shim shipped |
| Threadfin and Cabernet | 14 | Written setup flow; reproducible image/endpoint lock pending |
| Samsung TV Plus and custom sports playlist adapter | 14 | Gap: maintained provider/adapter validation needed |
| External EPG/XMLTV feeds | 14 | Written matching/freshness procedure; source rights/availability vary |
| WebGrabPlus | 14 | Legacy optional alternative; detailed current recipe pending |
| Nginx and local names | 15 | Written + host proxy template; TLS/container variant tests pending |
| Cloudflare Tunnel / remote HTTPS | 16 | Written flow; actual account/domain values deliberately excluded |
| Private overlay/VPN administration | 16 | Choice documented; vendor-specific recipe pending |
| Prometheus, node, blackbox and SNMP exporters | 17 | Written + schematic Prometheus config; service packaging pending |
| Jellyfin/application session exporter | 17 | Optional requirements; compatible exporter recipe pending |
| Dynamic container registry/metrics and health checks | 07,17 | Contract written; generic collector implementation gap |
| Grafana Overview/Servers/Network/Services/Public dashboards | 18 | Panel/query design; generic dashboard JSON not yet supplied |
| Alerts, webhook delivery and recovery tests | 18 | Written + simple rules example; clean delivery test pending |
| Disk SMART/USB/journal/capacity alerts | 19 | Written; collector packaging/version selection pending |
| Encrypted configuration/app backups, SQLite consistency | 20 | Written + restic alternative; automatic capture wrapper gap |
| Complete Jellyfin restore points, retention and mounts | 20–21 | Written requirements/drill; historical custom scripts not copied |
| Portable certificate-encrypted archives and split parts | 20 | Requirements/reconstruction design; generic encryption implementation gap |
| Offsite cloud copies and independent backup disk | 20 | Written verification workflow; scheduled uploader not shipped |
| Recovery and caretaker handoff | 21 | Written drill; measured recovery evidence pending |
| Media naming/imports/codecs/artwork/music metadata | 22 | Written bounded workflow; no destructive bulk tools |
| Duplicates, alternate editions, sidecars | 22 | Written review flow; no automatic deletion |
| Jellyfin custom CSS/logos/login notices | 23 | Written; original branding assets intentionally absent |
| Astro website, GitHub Pages, domains/HTTPS | 24 | Written; readers create original public-safe website |
| Independent public monitor/status page | 18,24 | Written provider-neutral flow; account-specific screens pending |
| Security/access review and exposure acceptance | 25 | Written test matrix |
| Private Markdown repo, access inventory/source data | 26 | Written + blank CSV/templates |
| Assisted operations/audits and change management | 26 | Written generic prompt and change template |

## How this becomes a repeatable release

Complete a new VM/host build from chapter 1 without consulting private source notes. Record exact versions and every missing command/UI step. Test one-host and two-host paths, reboot/missing-storage behavior, VPN isolation, sample workflows, notifications and isolated restore. Add generic config/scripts only after fixture/staging tests. Close gaps above and publish a tested release manifest; retain this draft label until then.
