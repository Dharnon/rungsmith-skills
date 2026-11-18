# Website previews and deployment

`list_catalog_examples` returns the independent examples used by the website: stable IDs, names, website anchors and preview availability. `get_examples` returns registered component parameters. They serve different purposes. A visible preview does not prove that source is available, dependencies are packaged or Designer import was verified.

## Native structure

Reuse a base component inside each example view. Keep synthetic state and the controls needed to exercise behavior in that example. Compose galleries from those same example views. Put page-only docking and navigation behavior on route hosts, never on the reusable examples. Preserve relative binding paths and per-instance message/popup IDs when extracting examples.

Perspective JSON does not run on Vercel as React. Interactive previews require a reachable Ignition Gateway with the required resources, styles, icons and project scripts. Visitors use supported browsers; they do not install a Designer or a Gateway to view a hosted demo. Importing a component into their own project is a separate workflow.

## Local versus hosted

- `local-only`: usable on the developer's computer, not a public URL. Never put localhost links in public setup instructions.
- `not-published`: offer the available screenshot or explanation; do not promise a live connection.
- `configured-hosted`: a deployment URL and component selection were configured. This is not evidence of successful browser rendering or load testing.

Hosted previews need a dedicated synthetic-data project, a stable HTTPS endpoint, WebSocket forwarding and an explicit route allowlist. Check iframe CSP/frame headers and session cookie behavior from the actual website origin. Provide a direct new-tab link for browsers that block embedded sessions. Test Safari, Firefox, Chromium and touch interaction before claiming compatibility.

Load examples on demand. Multiple iframes can create multiple Gateway sessions; offscreen unmounting releases browser connections and resets local demo state when reopened. Capacity limits and an inactive Gateway trial can prevent rendering even when the web page itself works. A successful iframe `load` event does not prove that Perspective connected, loaded the view, or is still online.

## MCP and skill hosting

The hosted MCP serves read-only registry and preview metadata. It does not render the components, operate a Gateway, grant Pro access, or deploy resources. A hosted transport token is a connection credential, not an entitlement. Never embed that token in client bundles, public installation examples or this skill.

Verify HTTP initialization, tools and skill package checksums on the deployed host separately from native preview rendering. A shared token supports an invited pilot; it is not a per-user account system, OAuth flow or public rate-limit implementation. Broader public access requires its own authentication/usage policy.

Use the project's configured preview and MCP endpoints. Do not invent a deployment domain or publish a local Gateway to make an unavailable preview appear live. Report verified behavior separately from pending hosting, licensing, capacity and browser checks.

Sources reviewed 2026-09-16:

- https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/perspective-sessions
- https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

### Catalog capacity and captures

Use actual native PNG captures for the initial catalog, not an HTML reconstruction labeled as Perspective. Record the exact example route, crop and capture date. Wait for painted content and reject empty screenshots before serving them. The catalog allows one selected interactive example per tab and unmounts hidden/offscreen frames; direct links and other tabs can still consume additional connections.

Local port 8103 has configurable `CATALOG_MAX_CONNECTIONS` (100 by default) and `CATALOG_HELLOS_PER_MINUTE` (600). The health response reports occupancy. These are proxy admission limits, not verified Gateway capacity. A simulated 100-socket test does not establish that a Gateway can sustain 100 sessions.

### Framing and catalog families

Group visual variants under their component family without renaming registered resource IDs. Metric Card includes the legacy KPI resource and Overview variants; preserve source/access contracts while using one website category and matching MCP anchors.

For dropdown examples, reserve room below the trigger inside the iframe. Remove lab-only card classes as well as inline borders: shared `!important` CSS can otherwise retain a second frame. Check the expanded menu at the actual embed dimensions, then refresh the closed-state native capture. Include validation text in its crop.

To contain wheel scrolling, set `overscroll-behavior` on the embedded document's `html` and `body`, scoped to an embed-only host. Applying it only to the iframe element does not stop scroll chaining. Verify both inside-wheel containment and normal outside-wheel scrolling.

A collapsed class on an outer shell is not equivalent to a class on its embedded sidebar. Scope selectors to the actual ancestor structure; preserve every navigation icon and accessible label while hiding visible text. Test expand and collapse after a Gateway scan.

Show a lock from the existing Pro access metadata. A lock is a display indicator, not an authorization mechanism; keep server-side source checks intact.
