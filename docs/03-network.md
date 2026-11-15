# 3. Gateway, switching, VLANs and Wi-Fi

**Run on:** gateway/switch/AP management UI from a local wired computer. **Requires:** private address worksheet and recovery/console access. **Produces:** predictable connectivity with a documented port map.

## Build a simple working LAN first

1. Save private exports/screenshots of current device settings. Label the cable from the ISP ONT/modem to the gateway WAN and from gateway LAN to switch. Record device models and firmware; menus differ by model.
2. Confirm the gateway serves DHCP on the intended LAN and routes to the Internet. Reserve addresses for media-node and apps-node by their NIC MAC addresses. Do not use an address inside an unmanaged DHCP pool without a reservation/exclusion.
3. Decide who provides DNS. During setup keep known working upstream DNS. After chapter 8, advertise your local resolver through DHCP and test one client before changing everyone.
4. If a mesh system sits behind the gateway, choose AP/bridge mode unless you intentionally need a second routed network. Do not accidentally run competing DHCP servers. Verify wired/wireless backhaul, roaming and placement with a client.
5. Disable Internet-facing device administration unless required and deliberately protected. Check IPv4 and IPv6 separately. Record remote-access recovery before changing management access.

## Optional managed VLAN design

Define each VLAN ID, subnet/mask, gateway, DHCP server, DNS, allowed flows and physical ports. Typical roles are management, servers, trusted clients and IoT. These are role names, not prescribed IDs.

Configure one test port first. An access port carries one client VLAN untagged; a trunk carries selected VLANs with a matching native/PVID policy at both ends. Keep management reachable while changing the uplink. Save running configuration to startup configuration using your vendor's supported procedure and verify persistence during a planned reboot.

Allow only required cross-VLAN flows: admin workstation → SSH/admin UIs; apps-node → media-node NFS and Jellyfin; clients → DNS and playback. Test permitted and prohibited flows. Include return traffic/stateful policy, IPv6 and multicast discovery requirements where applicable. Do not paste Cisco IOS configuration onto a business-switch UI or assume interface names match.

## Checkpoint and rollback

On each host check address/default route/DNS; from a client test gateway, SSH, a DNS lookup and Internet HTTPS. Confirm a non-admin/IoT client cannot reach management interfaces. Record cable/port/VLAN mappings. If locked out, restore via the retained console/local management path; change one device at a time.

Device-specific firmware/port screenshots are an open clean-room item; this chapter is a vendor-neutral procedure, not an exact router configuration.
