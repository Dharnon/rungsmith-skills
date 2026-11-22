# Native contracts, bindings and resource boundaries

Read this when creating or adapting a reusable view, diagnosing params, or validating generated resources.

## Start with version and ownership

| Boundary | Verify | Never assume |
| --- | --- | --- |
| Project vs Gateway | Are Views, scripts, Named Queries and styles in project resources? Are Tag Providers and connections Gateway-level? | That a project import includes Gateway-level configuration |
| Version | Exact target 8.1.x or 8.3.x, module version and actual source/export | That a snippet copied from another release serializes identically |
| View | `view.json`, `resource.json`, path, root container and actual component descriptors | That a hand-written illustrative JSON is importable |
| Contract | params, direction, defaults, host assignments and existing consumers | That a parameter name seen in a screenshot exists in source |
| Data | source path, transform, quality, timestamp and readback | That a valid-looking numeric value is currently good |

Manual: [Views in Perspective 8.3](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/views-in-perspective); [Perspective Component Properties 8.3](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/perspective-component-properties).

## Instance-boundary rule

The manual explicitly states that a property binding cannot directly reference a property of a **different View instance**. Pass data across that boundary using the child View's declared `params` and the host's Embedded View `props.params`. Verify the param direction (input, output, in/out) before wiring it; changes can break older consumers.

Manual: [Property Bindings in Perspective 8.3](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/property-bindings-in-perspective).

### Walk one reusable instance

Fixture-only target (not a claim about the Rungsmith catalog):

- Child View: `Training/EquipmentSummary`
- Input parameter: `equipmentId`
- Parent: two native Embedded Views (component type `ia.display.view`), each `props.path = "Training/EquipmentSummary"`
- Host passes `props.params.equipmentId = "P-204A"` and `"P-204B"` respectively
- Child shows its received ID using a supported property binding

**Expected:** first mount displays A and B. Update B's host parameter to P-301: A stays A, B becomes P-301. Reverse the host order and open B: the selected ID remains B, not the former row index.

Do not treat the above pseudo-configuration as a complete view JSON. Create or update resources using real exported source, Designer or the version-matched resource API, with backups and validation.

## Select the right binding

| Source/need | Native mechanism | Hazard to check |
| --- | --- | --- |
| Same-view property | Property binding | Cannot bypass a child-view boundary |
| Direct equipment tag | Tag binding | Provider/path, quality, access and refresh |
| Reusable equipment path | Indirect tag binding or a verified expression binding | Placeholder/param value and missing path |
| Derived display | Expression or transform | Null handling and whether quality remains visible |
| Query-backed display | Named Query binding | Query parameter ownership, load/error states, repeat query cost |
| Historical plot | Tag History binding | Time window, aggregation, interpolation vs raw samples |
| Cross-view intent | Declared param or scoped message (as appropriate) | Instance identity, handler scope, duplicate receivers |

Tag binding modes (direct, indirect, expression), overlay behavior and transforms: [8.3 Tag Bindings](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/tag-bindings-in-perspective), [8.3 Transforms](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/transforms).

### Safe data-flow worksheet

Use these headings on a real project:

`Source tag/query or fixture: ...`
`Host owner (view path / component path): ...`
`Child path and param direction: ...`
`Binding and transform on display: ...`
`Quality/timestamp available to UI: ...`
`Potential write target: NONE / verified path ...`
`Other consumers to regression-test: ...`

Avoid substituting `coalesce(x, 0)` or an equivalent default when a non-good quality state would need to remain visible. Check the original QualifiedValue and overlay policy separately.

## Script vs expression boundary

Ignition Perspective scripting uses Jython, not browser JavaScript, and script execution is handled by the Gateway even for Perspective Session interactions. Choose expression/property bindings for simple derivations where supported; use scripts for logic that actually needs them. Do not generate Python 3-only syntax such as f-strings without verifying a separate non-Jython runtime.

Read-only illustrative Jython **for an authorized test Gateway**, not a command/control snippet:

```python
# Within a permitted Gateway/Perspective scripting context.
qv = system.tag.readBlocking(["[default]Sim/P204A/Running"])[0]
if qv.quality.isGood():
    displayValue = qv.value
else:
    displayValue = None  # UI must separately expose invalid quality
```

The tag above is an illustrative fixture path, not an assertion that it exists. Reading or writing real tags must use paths discovered in the actual project and the current user's permitted scope.

Manual: [Scripting in Perspective 8.3](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/scripting-in-perspective).

## 8.3 API is not a substitute for contract validation

For gateways exposing 8.3 Resource APIs, discover the actual resource type and schema through the Gateway's `/openapi` and read the resource before proposing updates. Prefer a candidate workspace or development Gateway, preserve existing unknown fields, require an expected revision/hash where available, and record a diff. An HTTP 2xx confirms a request outcome, **not** a rendered, working or authorized industrial screen.

Manual: [Ignition 8.3 OpenAPI](https://www.docs.inductiveautomation.com/docs/8.3/platform/gateway/openapi).
