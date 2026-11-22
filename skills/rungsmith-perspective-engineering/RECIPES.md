# Repeatable native Perspective recipes

These are **test specifications**, not finished importable component packages. Replace fixture IDs, paths and properties using real source exported from the target Designer. Never infer a registry contract from a sample.

## Recipe A — Reusable pump summary with two independent instances

**Goal:** a child view follows its host's asset identity without coupling other instances.

**Prerequisites:** an authorized *development* project, known target Ignition version and a small host view. No PLC or production data connection needed.

**Fixture:**

| Instance | ID | Running | Fault | Flow | Quality |
| --- | --- | --- | --- | --- | --- |
| First | P-204A | true | false | 42.7 L/s | Good |
| Second | P-204B | false | true | unavailable | Bad |

1. In Designer create `Training/EquipmentSummary` with declared input `equipmentId` (and separately defined test-data inputs if needed). A Label shows `equipmentId`. Keep the display-only fixture explicitly labeled synthetic.
2. Create `Training/EquipmentHost` with two Embedded Views, both pointing to the child via `props.path` and each supplying its own `props.params.equipmentId`.
3. Bind state, flow and quality to their *own* instance's fixture, not to a shared session property. Show “Unavailable” for the second flow instead of zero; do not bury its Fault state behind Bad flow.
4. Update only the second instance from P-204B to P-301 and observe both children.
5. Add two rows for A/B to a repeater (if used), reverse their order and open the details for B. Verify the identity passed to the detail.
6. Test narrow viewport, long name and a disabled control; do not introduce a process write for the fixture.

**Expected:** first child remains P-204A; second becomes P-301 on host update. After row reorder the selected asset in detail matches the clicked item's *stable ID*, not its prior array position. Unknown quality is displayed. No commands or tag writes are emitted.

**Block if:** both children change together, output claims live data, an unavailable reading becomes zero, or the detail opens for a different ID.

**Evidence:** before/after host and child paths, param contract, the two actual displayed IDs, target version, optionally screenshot/session trace. Mark “not runtime-verified” if no session was opened.

## Recipe B — Popup opened before its async parameter arrives

**Goal:** prevent an early click from operating on stale Designer defaults.

**Fixture timeline:** source screen previously selected P-204A. Navigation requests P-204B. Parent/child binding is delayed in a development fixture; in the interim the child's effective asset ID is unset or still A.

1. Inventory the launching component, requested ID, child `params`, native popup view path and recipient handlers.
2. Decide readiness from an **explicit validity check** of the ID and any data dependencies needed to act. Disable the action before readiness; do not merely fade/cover it.
3. Open the page and click immediately, then once B's valid params resolve; record the popup/command target in both cases.
4. Close/reopen rapidly, then repeat with two different child instances and with two panels representing the same asset but distinct instance keys.
5. Check handler scope: page-scoped messages may reach multiple handlers. The intended receiver must filter correctly when actions are instance-specific.

**Expected:** no wrong-asset action during loading. Once ready, B opens and all data sources use B. Only the initiating instance handles any instance-specific event.

**Block if:** click opens A, a visual-only disabled state still calls an action, a second instance processes the event, or an arbitrary animation delay is the only protection.

**Sources:** [Parameter arrival issue](https://forum.inductiveautomation.com/t/passing-params-in-view-issue-what-to-do-about-the-delay/84285), [8.3 Component Message Handlers](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/scripting-in-perspective/component-message-handlers).

## Recipe C — Determine whether a trend is slow or merely hidden

**Goal:** evaluate a performance repair by observing real operator milestones.

**Fixed environment:** same Ignition version, exact view revision, dataset size, history window, viewport, browser/client and comparable Gateway load.

1. Capture launch, shell visible, correct identity, first good reading and first usable trend at least three times cold and three times warm.
2. In development substitute a time/size-matched history fixture while preserving the chart and transforms. Re-run.
3. If the discrepancy follows the live source, inspect request execution, transport and transformation individually. If the chart remains slow with fixture data, inspect render cost and mounted repeated views.
4. If lazy-loading the history tab, test both initial faceplate and *first history open*: improving the former may worsen the latter.

**Expected:** comparative timing table with trials, conditions and a narrow cause statement. The trade-off is explicit.

**Block if:** faster fixtures are called “SQL fixed” without isolating query time, hidden charts are assumed unmounted, or bad-quality overlays are suppressed as a performance workaround.

**Sources:** [Perspective performance forum](https://forum.inductiveautomation.com/t/performance-optimization-findings-for-perspective/79229).

## Recipe D — Convert a visual reference into native UI without fake parity

1. Classify each referenced feature as: native component property, native Style Class, scoped `stylesheet.css` rule, custom module, website-only or unverified.
2. Inspect the actual project and component registry contract before choosing a substitute.
3. Prototype one operator journey with readable data/identity/states at desktop and touch sizes. Keep motion incidental to important process changes.
4. Test supported focus, click, keyboard, quality overlays and actual native navigation/message handlers in the target client.
5. Report what was reproduced exactly, approximated, deferred or unsupported. A rendered HTML preview is visual evidence only, not an import test.

Use `rungsmith-web-to-native` for the feasibility pass and `rungsmith-native-ui-quality` for the operator critique.
