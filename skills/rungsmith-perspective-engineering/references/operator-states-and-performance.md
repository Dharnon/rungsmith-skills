# Operator states, interaction truth and performance

Read this for industrial HMI reviews and for faceplates, repeaters, trends or controls connected to real process data.

## Make the important state unmistakable

Test a single screen in these conditions using **realistic, explicitly simulated fixtures** when live data is unavailable:

| Condition | Fixture | Must remain visible |
| --- | --- | --- |
| Normal | P-204A running, good quality, 42.7 L/s | Identity, unit, timestamp/freshness, state |
| Fault | P-204B faulted, running indication also present | Fault priority, affected asset, action path |
| Bad quality | P-204A value unavailable/Bad | An explicit unavailable/quality indicator, not “0.0 L/s” |
| Stale data | Last timestamp significantly older than expected scan | Measured-at vs viewed-at, state of freshness |
| Loading | Child param not yet resolved after page opens | Disabled action, placeholder identity, no previous asset |
| Empty | No rows/history points in selected period | Explicit empty state, no fabricated line |
| Interlocked | Command denied by policy/interlock in fixture | Disabled command *and* actual command-path block |
| High density | 20+ equipment entries; uneven labels and value lengths | Scannable grouping, comparison and stable selection |

Treat fault/quality/staleness as separate dimensions, not a single “red/green” bool. Show the source of an alarm condition and acknowledge/shelve state where relevant; visual silence must not imply that alarms are healthy.

## Do not solve loading races with decoration

[Forum: Passing params in view issue](https://forum.inductiveautomation.com/t/passing-params-in-view-issue-what-to-do-about-the-delay/84285) describes a nested Perspective view that briefly used an old default parameter. The reported suggestion is to validate readiness, disable the action until new params are valid, and consider non-persistent values for fields that should not retain Designer defaults. Do not rely on an arbitrary fade delay to prevent a wrong-equipment action.

**Regression:** immediately after opening the page, click the second equipment control; if its effective ID is not known and validated, the action remains unavailable. Once B arrives, activation must target B. Retest after reorder and popup reopen.

## Performance investigations must change one factor

[Forum: Performance Optimization Findings](https://forum.inductiveautomation.com/t/performance-optimization-findings-for-perspective/79229) reports nested Embedded Views, repeated individual tag reads and expressions as possible overhead sources. These are **diagnostic leads, not universal limits**: do not present “at most two levels” as a documented hard cap.

Measure four timestamps under a fixed dataset and client: launch → shell visible → correct asset identity → first valid reading. Add first usable history interaction if the view includes a trend. Record cold, warm and repeated open results (at least 3 comparable trials when available). Note number of repeated child views, active queries/subscriptions and Gateway load.

Choose one controlled contrast:
- Replace live history with a size-matched fixture; same chart settings and viewport.
- Reduce repeater count while holding each instance constant.
- Temporarily eliminate nonessential motion without changing action wiring.
- Compare a single batched read to repeated reads when the script is actually under your control.

If performance changes, state the *narrowest supported conclusion*. Faster local fixture data does not yet prove slow SQL; further distinguish database execution, network, transform and rendering. Do not mask bad-quality overlays solely to improve perceived load time.

## Styling limits

Use native Style Classes for reusable semantics. In Perspective's `stylesheet.css`, CSS class selectors corresponding to Perspective Style Classes use the `.psc-` prefix. Avoid global selectors targeting undocumented internal DOM and do not assume a browser prototype's CSS is a supported Designer property. Compare normal/fault/bad-quality at narrow and desktop widths. Respect reduced-motion preferences where the deployed runtime supports them and prioritize stability over motion on alarm or process readings.

Manual: [Style Classes 8.3](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/styles/style-classes).

## Process action = intent + permission + readback

For any **explicitly authorized** command integration, trace:
1. The operator intent, asset and relevant setpoint.
2. Authentication/authorization plus existing Gateway/controller interlock enforcement.
3. Actual command outcome, including error/rejection.
4. Observed process readback and its quality/timestamp.
5. Visible difference between “requested”, “accepted” and “measured”.

Do not claim a button color, local optimistic state or change in a view param proves a motor started. Default to display-only fixtures unless the user provides the actual authorized command system and a dev test plan.
