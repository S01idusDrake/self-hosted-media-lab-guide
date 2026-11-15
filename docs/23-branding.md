# 23. Optional Jellyfin web branding

**Run on:** Jellyfin administrator browser. **Requires:** working default UI and a saved private copy of existing branding settings. **Produces:** original branding that can be removed without reinstalling.

1. Create or obtain a logo you have rights to use. Make light/dark versions if needed; export a web-friendly SVG/PNG and a small icon. Check contrast at the intended header size. Do not reuse another installation's artwork, name or external asset URLs.
2. Host the asset on your own controlled HTTPS site or supported static asset location. Verify it is reachable without authentication and has correct content type. Remote assets can reveal client requests to their host; keep this in mind when choosing hosting.
3. In Jellyfin Dashboard branding settings, save existing custom CSS/disclaimer first. Add one small new block at a time. Use your selected Jellyfin Web version's actual selectors rather than assuming an old theme's markup.
4. If changing an image/background with CSS, scope it to the intended header/login element and preserve accessible text. Do not hide authentication warnings, controls or account state. Use your own generic name and asset URL; no CSS from an existing private installation is included here.
5. Test logged-out login, logged-in header, navigation, high zoom, phone/tablet/desktop widths, light/dark mode and keyboard focus. Confirm media controls and menus still work.
6. Add optional login guidance in neutral wording without secrets or internal addresses. Keep browser favicon and native app branding separate; custom web CSS does not automatically change those clients.

Checkpoint: screenshots show readable layout at representative sizes, no horizontal overflow or hidden controls and no console mixed-content errors. Roll back by restoring only the saved branding block/settings, preserving any unrelated later edits. Recheck after Jellyfin Web updates.
