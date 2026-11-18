---
name: rungsmith-perspective-css
description: Build or repair scoped CSS, themes, tokens, responsive layouts and overflow in native Ignition Perspective. Use for stylesheet and visual parity work; distinguish component properties from browser-only techniques.
metadata:
  status: preview
  native-verification: pending
---

# Perspective CSS

Identify the target version, active project stylesheet, native view and actual host dimensions. Read current runtime resources before changing a repository copy; Designer saves may be newer. Preserve unrelated rules and back up resources being replaced.

Start at the layout contract. Inspect parent sizing, grow/shrink, basis, min/max dimensions, embedded-view default size and scroll ownership before adding CSS. A collapsed child or overflowing flex item often requires native position/layout changes. Do not conceal a broken layout with overflow:hidden or absolute offsets.

Use project style classes and scoped custom properties for reusable tokens. Map light/dark surfaces, foregrounds, borders, focus and semantic states. Keep process significance independent of the decorative accent. Avoid global ia.* overrides unless explicitly requested and checked across affected components; prefer opt-in scope. Keep an explicit visible focus treatment even when removing the default blue outline.

Inspect the rendered component structure in an actual client when a selector depends on native chrome. Prefer owned classes over generated indices, nth-child and unstable runtime identifiers. Check specificity before escalating !important. Consolidate an owned rule instead of appending successive overrides.

Declare which element scrolls in each axis. Resolve nested scrollbars by sizing the intended scroll container; retain keyboard access and visible overflow affordances. Thin scrollbars must remain usable in high-contrast settings. Test long content, empty content, zoom, narrow width and translated labels. Avoid fixed heights that clip values or units.

For a catalog iframe, identify host-page, iframe-document, Perspective dock and inner-table overflow separately. Host CSS cannot cross the iframe boundary. A proxy-injected preview stylesheet is not a packaged native fix; record that delivery dependency and verify the matching selectors against the rendered client before claiming docks were removed.

For modern CSS, check target browser/Workstation support and a supported fallback. Browser support does not grant control over Perspective's DOM or JavaScript lifecycle. Keep native layout as the baseline; apply advanced CSS only where it solves the requested problem and stays scoped.

Verify actual route, viewport and state. Check computed geometry, keyboard focus, light/dark contrast and neighboring components. Separate file/schema checks from native runtime observations. State any untested client/version.
