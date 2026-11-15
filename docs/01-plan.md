# 1. Plan the build

**Run on:** paper or admin workstation. **Requires:** a list of equipment and data worth protecting. **Produces:** a completed private worksheet, budget and acceptance scope.

## Decide what you need

1. Choose one or two hosts. Reuse supported hardware only after checking disk and network health. Record CPU, RAM, system-disk capacity and supported Linux release. Leave resource headroom for transcoding and monitoring history.
2. Estimate current media size, yearly growth and simultaneous streams. Transcoding needs depend on codecs, subtitles and clients; do not size from resolution alone. Put databases on SSD and plan cooling, reliable power and secure USB placement.
3. Separate system, media and backup storage roles. A backup disk attached to the same host does not cover theft or a host-wide incident; keep an additional offsite copy for important configuration/data.
4. Identify irreplaceable personal media separately from replaceable files. These guides do not include content or source subscriptions. Only acquire and share content you are entitled to use.
5. Pick an IP reservation for each role, management access, optional VLANs and a domain if you need public HTTPS. Avoid subnet overlap with networks you connect through remotely.
6. Choose which optional modules to skip. A VPN downloader is not required for Jellyfin; IPTV, music requests, Soulseek helpers, public access and the website are independent extensions.
7. Copy `templates/build-worksheet.md` and `templates/inventory.csv` outside this repository. Fill in your actual values privately. Keep passwords/API keys in a separate vault, recording only the vault item name.

## Select versions deliberately

Use maintained releases supported by your OS and CPU architecture. For containers, choose a release tag, read its migration notes, pull it, then record its registry digest in the private version inventory. Do not assume a floating `latest` tag is reproducible. This draft does not ship a tested version lock for every module.

## Checkpoint

You can identify every disk that must be preserved, every device that may be erased by an installer and how you will recover access if the network changes. If any answer is unclear, stop before installing. No disk erase is implied by following this book.

Source: [Jellyfin hardware guidance](https://jellyfin.org/docs/general/administration/hardware-selection/). Exact equipment choices remain yours.
