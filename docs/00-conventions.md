# How to use this book

## Understand the roles

`media-node` is the Linux computer holding the media disks and running Jellyfin. `apps-node` runs Docker services. Your `admin workstation` is the computer used to connect to them. A one-computer build combines both roles; Docker service-to-service addresses still differ from host addresses.

A terminal is a text interface. Enter one command at a time. A line starting with `#` in a shell block is a comment. Output belongs below the command, not back in the terminal. `sudo` runs a command as an administrator; read the command before supplying your own password locally. Never send passwords to a helper/chat.

`<PLACEHOLDER>` means replace the whole placeholder before using it. Angle brackets are special shell syntax, so examples containing them are **not executable as written**. Shell variables such as `$MEDIA_IP` work only after you set them in that terminal. `${NAME:?message}` in Compose stops validation until a variable has been set. `.example` files are worksheets, not active secrets or deployment files.

`127.0.0.1` means this host or this container, depending on where the request runs. A container's localhost is not the Docker host. `radarr:7878` is a Docker service name available on a shared Docker network. `example.net` is a reserved documentation domain; replace it with a domain you own. A `.test` name is for internal testing and is not a public certificate target.

## Separate creation from observation

Read commands inspect state: `hostnamectl`, `ip -br address`, `systemctl status`, selected logs. Change commands install packages, edit settings, start services or write files. Installation chapters describe changes to a new lab. They do not authorize changing someone else's lab.

Before editing an existing file, make a private dated copy, identify who depends on it and keep console access. Use an editor you understand (`sudoedit /path/to/file` is one option). Save, run that service's configuration validator, then apply. If validation fails, restore the saved file; do not keep restarting a broken service.

Never use `chmod -R 777`, recursive ownership changes, `docker compose down -v`, blind volume pruning, formatting or partitioning commands as a troubleshooting shortcut. A mount can hide files already under its directory. A listed mount can also be stale after USB loss. Both require investigation.

## Keep records

For every acceptance check record the command or UI action, time/timezone, expected result, actual result and software version in a private copy of the acceptance template. A web page loading does not prove a completed workflow. End each chapter with its checkpoint, and keep secrets out of screenshots and logs.

If a command is missing, stop and install it through your distribution's documented package manager; do not paste an unexplained remote script. For a disk showing I/O errors, stop normal setup and use the preservation guidance in chapter 19. Do not run the chapter's scratch-file tests on suspect storage.
