# 8. Private DNS with AdGuard Home

**Run on:** apps-node and one test client. **Requires:** static/reserved host IP and a recovery resolver plan. **Produces:** working DNS without exposing administration.

1. Identify what already listens on TCP/UDP 53 with `sudo ss -lntup`. A local OS stub resolver can conflict with a new listener. Do not disable the OS resolver without documenting an alternative and a recovery path.
2. Select the official AdGuard Home image/release. Create separate persistent `work` and `conf` directories per its Docker instructions. Bind DNS TCP/UDP 53 only to the chosen server LAN address. Initially bind the setup UI to loopback and reach it by SSH tunnel. Avoid host networking unless deliberately required.
3. Start the container and finish the setup wizard. Choose the intended interfaces and UI port; change initial credentials. Record the final UI address privately. Configure upstream resolvers, blocklists and logging/retention according to your household's privacy needs.
4. Test a public lookup explicitly against the new resolver: `dig @<APPS_IP> example.net A`. The response should be valid rather than timeout/SERVFAIL. Test both UDP and TCP, a blocked test domain selected from your configured list and a permitted domain. This is not proof that every client uses the resolver.
5. Add DNS rewrites for private admin names you chose, pointing to the reverse proxy host. Use `.test` for a purely internal test zone or a subdomain you own. Keep public Requests names resolving to their intended HTTPS ingress if you rely on public TLS; do not create a split answer that breaks certificate/proxy assumptions.
6. Change DNS on one test client, reconnect/renew its lease and confirm which resolver it actually uses. Only then update gateway DHCP DNS. Check IPv6 router advertisements and encrypted DNS behavior separately. A second public resolver may let clients bypass filtering; it is not equivalent to a redundant local filtering resolver.
7. Add a lightweight check of the UI and a DNS response through the intended listener. Keep DNS health separate from the UI HTTP check. Back up config and filtering choices, excluding unnecessary query history.

Checkpoint: restart preserves configuration, a client resolves public/private names, DNS recovers after reboot and the admin UI is restricted. Roll back the DHCP/client DNS setting first if resolution fails, then diagnose the server. Keep a record of the old DNS values privately.

Source: [AdGuard Home Docker guide](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker).
