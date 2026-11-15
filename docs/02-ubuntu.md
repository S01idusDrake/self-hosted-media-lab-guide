# 2. Install and verify Ubuntu Server

**Run on:** local console of each new host; later, admin workstation for SSH. **Requires:** backed-up existing data, verified installer and console access. **Produces:** a supported Linux host with stable identity.

## Install

1. Download an Ubuntu Server LTS image supported by your hardware from Ubuntu's official site. Verify its checksum using the official release instructions. Create installer media with a trusted tool. Writing the installer USB erases that USB; confirm its identity.
2. Disconnect media/backup disks during OS installation where practical. This reduces the chance of selecting the wrong disk. Record which disk remains attached for the OS.
3. Boot the installer. Set locale, keyboard and network. Use DHCP initially; later reserve the address in your gateway. Choose role hostname `media-node` or `apps-node` (or your own name).
4. At storage selection, compare model/capacity with your worksheet. Installation/partitioning can erase the selected disk. Proceed only after deliberately approving that target; this guide provides no blanket formatting command.
5. Create your own non-root administrator. Enable OpenSSH if offered. Do not install optional server snaps merely to match this book. Complete installation, remove installer media and reboot from the OS disk.
6. Sign in at the console, then inspect:

```sh
hostnamectl
cat /etc/os-release
ip -br address
ip route
timedatectl
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
```

Confirm hostname, release, NIC, gateway, time synchronization and boot disk. Keep serial/UUID output private.

7. Update the new OS:

```sh
sudo apt update
sudo apt upgrade
```

Read the proposed changes. Reboot during your setup window if required, and confirm the host returns. Set your chosen timezone with `sudo timedatectl set-timezone <REGION/CITY>` only after replacing the placeholder.

## Hardware branches

For Intel Macs, verify Ethernet, boot and graphics support on your exact model. For Wi-Fi adapters, identify the chipset and follow the distribution's driver guidance; do not reuse another machine's blacklist/kernel changes. Prefer wired Ethernet for storage. An unsupported device is a compatibility gap, not a reason to disable broad security protections.

## Checkpoint and rollback

Verify a second login and a reboot before attaching data disks. Retain installer/recovery media and console instructions. If boot/network fails, use the console; do not repeatedly reinstall over media disks.

Source: [Ubuntu basic installation](https://ubuntu.com/server/docs/tutorial/basic-installation/).
