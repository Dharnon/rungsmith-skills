# Acceptance checks

1. Confirm every Embedded View path exists and every supplied param passes the current contract. Check enum values and parameter direction in source.
2. Compare resource hashes with the supplied snapshot; include its named styles and resolve shared CSS separately.
3. Exercise click, keyboard, disabled state and actual message handlers in the real Perspective client. A native-looking HTML preview does not pass this check.
4. Check desktop and tablet widths, clipping, overflow, touch targets, focus and state labels. Keep the user's chosen palette and component styling unless the requested task changes them.
5. State which checks were performed: static parsing, archive contents, Designer import, Gateway refresh, connected native client. Do not infer runtime acceptance from a successful HTTP request or screenshot.
