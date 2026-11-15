# 4. Administration, SSH and secret handling

**Run on:** admin workstation and each host. **Requires:** verified host address and console. **Produces:** tested key-based access and a private credential inventory.

1. On the workstation, check whether you already have an appropriate SSH key. If creating one, use `ssh-keygen -t ed25519` and a passphrase. Do not overwrite an existing key. Keep the private key on the workstation; only its `.pub` partner belongs in a server's authorized keys.
2. Verify the host's SSH fingerprint from its trusted console before accepting it. A changed fingerprint needs investigation, not automatic removal of trust records.
3. Install your public key with your OS's supported SSH key-copy method. Test a second terminal login before changing password authentication. Record an emergency console route; do not disable every recovery method at once.
4. Create optional workstation SSH aliases in your private `~/.ssh/config`:

```sshconfig
Host media-node
    HostName <MEDIA_IP>
    User <ADMIN_USER>
    IdentityFile ~/.ssh/<YOUR_KEY_FILE>

Host apps-node
    HostName <APPS_IP>
    User <ADMIN_USER>
    IdentityFile ~/.ssh/<YOUR_KEY_FILE>
```

5. From the workstation, use `ssh media-node` and `ssh apps-node`; run `hostname` to confirm each target. Restrict SSH in your firewall to administrative networks and verify an existing session remains open during rule changes.
6. Create private vault entries for host administration, registrar/DNS, VPN, app recovery administrators, backup keys and notifications. Never commit real `.env`, application databases, tokens, webhook URLs, raw router exports or screenshots showing them.
7. For localhost-only web services, use an SSH tunnel. Example: `ssh -N -L 7878:127.0.0.1:7878 apps-node`, then visit `http://127.0.0.1:7878` on the workstation. Keep the terminal open; Ctrl-C closes the tunnel. Select a different local port if already occupied.

## Checkpoint

Both aliases reach the intended host, a second session works and you can recover from console. Document access owner and vault references privately. Do not put a private SSH key on the application host for convenience or expose SSH directly to the Internet as a default.
