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

Practice this workflow in a development project: [Find which box owns unwanted scrolling](RECIPES.md).

## Debug overflow at the embedding boundary

Reproduce clipping with the same view embedded at the failing width. Inspect the host container type and child position first, then the Embedded View's default width and height flags, child root layout and overflow rules. Find the first box that exceeds its available space. Changing overflow on the last box can conceal a missing command or quality label.

Test a short equipment label and one with a long distinguishing suffix. Check both with the page dock expanded. Preserve access to the suffix and the unit while allowing the intended container to scroll. Verify a second consumer at normal width and identify which change belongs to the host versus the shared child.

## Diagnose a rule that wins in one host only

Compare the same child in its normal page, popup and embedded host. Record applied style classes, theme, inline property values and the nearest ancestor on which the rule depends. Find the winning declaration in the rendered client when available. A rule can be present in all three contexts and match only one because the expected ancestor lives outside the popup.

Choose the narrowest owner that actually spans the intended contexts. A fix for every instance belongs on a child-owned class. A compact variant for one host needs an explicit opt-in that the child can consume. Verify the default instance alongside the opted-in one. Restore temporary diagnostic styles and check focus and overflow after the change.
## Trace a layout defect from boundary to boundary

Start at the first incorrect rectangle. Inspect the available size in the host, the child's assigned position, the Embedded View's sizing configuration, the child root and the content that overflows. A scrollbar at the final table can originate several ancestors earlier. Change one boundary at a time and record the first change that restores access to the clipped content.

Check the cost of the fix on another consumer. A global overflow rule can make one screenshot cleaner while hiding the only way to reach a command in a small popup. A child-wide minimum width can repair a workstation layout and break a docked tablet view. Prefer an explicit compact layout or host-specific opt-in when these contexts genuinely require different arrangements.

## Work through the available-height budget

A fixture popup has 480 px of usable content height, a 64 px header and a 56 px footer. Before gaps and padding, the body can use 360 px. If an embedded child insists on its 420 px default height, at least 60 px must overflow or displace another region. Inspect the native parent's position settings, embedded default-height configuration and the intended body scroll region in that order.

Add the actual margins, padding and any validation text that appears outside the body. Measure again after zoom or a translated heading wraps. Choose one intentional vertical scroll owner. Keep the header and footer stationary only if the resulting body remains usable; a very short viewport may need the whole panel to scroll. Verify the last field and the dismissal path with keyboard and touch.

Record the measured height at each boundary, the first overcommitted child and which region remains scrollable after the fix.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The last row is inaccessible although no scrollbar appears | Inspect the first ancestor clipping overflow and the actual scroll owner. | Restore a reachable scroll surface and verify keyboard access. |
| A new stylesheet rule affects a different popup | Inspect which custom class or global selector both surfaces match. | Narrow the selector to the intended owned component or variant. |
