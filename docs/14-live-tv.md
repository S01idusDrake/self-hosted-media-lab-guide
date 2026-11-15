# 14. Live TV, playlists and guide data

**Run on:** apps-node UIs and Jellyfin dashboard. **Requires:** authorized M3U/XMLTV sources, stable connectivity and an explicit channel plan. **Produces:** a small tested live-TV pipeline.

## Understand the pieces

M3U lists stream URLs. XMLTV describes programme schedules. Threadfin can proxy/map playlists and guide data into a tuner-style service. Cabernet can aggregate supported sources through plugins. Neither creates rights to watch a source, and a guide generator is not a video server. Use the fewest components your sources need.

1. Choose a direct Jellyfin M3U/XMLTV path, Cabernet aggregation, Threadfin mapping, or a deliberately documented combination. Draw the exact source → aggregator → tuner → player path; avoid loops and duplicate channel IDs.
2. Select current releases from upstream. Persist each project's documented config/data directories on local SSD and limit administration to loopback or your management network. Verify actual ports and image architecture rather than assuming old defaults.
3. In Cabernet, enable only the needed maintained source plugin and configure its supported settings privately. Begin with a few channels. Record playlist/guide endpoints from the UI, not guessed URL patterns. Confirm the guide downloads and contains programme entries with correct timezone/channel IDs.
4. In Threadfin, add a single selected M3U and matching XMLTV source, map channel identifiers, apply a minimal filter and set realistic tuner limits. Test its own lineup/status and preview before connecting Jellyfin. Avoid exposing provider URLs containing credentials in screenshots.
5. In Jellyfin Live TV, add the supported tuner/M3U and guide URL from the chosen component. Configure refresh schedule and channel mapping. Fetch a small guide, then play a channel for several minutes and test switching channels. Check a recording only if you plan recordings and have a healthy destination/reserve.

## Optional source adapters

Samsung TV Plus and other public/free services may need region-specific third-party adapters. Choose a maintained authorized adapter yourself, verify upstream license/terms, image provenance, refresh behavior and returned media URLs. No exact adapter image/version was established for this generic edition, so this module is a documented gap rather than a ready Compose service. A custom sports playlist endpoint is similarly an optional source adapter: define source rights, format, refresh/cache lifetime and availability checks; do not scrape arbitrary sites as a default.

EPGShare or another external XMLTV feed must match your channel lineup/region. Check current licensing/availability and freshness. Old guide timestamps can make a working tuner look empty. Keep external-source failure separate from local application health.

## Legacy alternative: WebGrabPlus

Use WebGrabPlus only when your selected supported guide source requires it. Follow its current installation/licensing and site-configuration instructions, persist generated guide/config privately, schedule refresh and point the consumer at the resulting XMLTV. Verify at least one programme/channel. Do not add it to a build already using a sufficient guide path; retirement means removing actual references first, then preserving config before stopping the component.

Checkpoint: app health, playlist retrieval, fresh guide, correct mapping and actual playback pass. A web UI responding is insufficient. Roll back a new source/mapping without deleting working IPTV configuration.

Sources: [Threadfin](https://github.com/Threadfin/Threadfin), [Cabernet](https://github.com/cabernetwork/cabernet). Provider adapters and WebGrabPlus require separate current-version verification before a repeatable release.
