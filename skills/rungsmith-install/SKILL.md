---
name: rungsmith-install
description: Install or update a Free Rungsmith native Perspective component from its verified package and contract. Use for catalog AI prompts, imports and dependency wiring; not for website previews or production deployment.
metadata:
  version: "1.0.0"
---

# Install a native Rungsmith component

Inspect the target Ignition version, project resources and reusable view paths before changing files. A hosted MCP cannot inspect the local project or import into Designer.

1. Read get_catalog_component with the exact catalog id and includeSource: true. Read list_catalog_examples for the requested example. If the id is registry-only, use get_component, get_component_source and get_install_instructions. A missing or locked response is a stop condition for source installation, not permission to reconstruct it.
2. Read the returned parameter defaults, input/output/inout directions, dependency files, stylesheet snippet and README. Use the returned artifact and SHA-256 values. The screenshot is a usage reference, not the contract. An example may share the same reusable source with other variants.
3. Preserve existing project files. Import the package into the requested development project with native resource descriptors and paths intact. Compare the supplied styles with the installed rules. Add missing rules once, merge upstream changes with local overrides, and leave an identical snippet in place on reinstall. Embed with ia.display.view and the returned props.path and props.params. Handle duplicate view paths before replacing anything.
4. Wire outputs and process commands in the owner view according to the actual contract. Sample controls are not evidence of PLC integration. Do not perform tag writes or operate equipment without the user's authorization.
5. Validate JSON and references, then test in a native Perspective client. Report package integrity, Designer import and runtime verification separately. For an update, compare the old and new contract and preserve local customizations; never overwrite a customized package merely because a newer version exists.

Without MCP, use /api/catalog/{id}?format=markdown on https://www.rungsmith.dev and follow its actual download link. Do not invent an npm or shadcn installer for Perspective. MCP retrieval is read-only; use authorized local tools to make changes.

Practice this workflow in a development project: [Reinstall an unchanged revision](RECIPES.md).

## Rehearse an upgrade with a consuming view

Inventory the existing embedded-view paths, parameter overrides, named style classes and project scripts used by one real consumer. Compare the candidate package to that inventory before import. A resource with the same path can have a different parameter direction or an added dependency even if the preview looks unchanged.

Import into a development copy and open the existing host alongside a fresh example. Exercise a non-default parameter and observe the documented output in each. For missing styles, distinguish an absent stylesheet snippet from a consumer override. Record the package revision, imported paths, local deviations and result of reopening the host in a launched session.

## Diagnose a successful import with a blank embed

Start with the exact installed resource path and the Embedded View's configured path. Inspect parameter names, direction, required dependencies and the child root dimensions. Open the installed child directly with known example parameters. If that works, compare the same parameters inside the consuming host. If it is blank in both contexts, check missing dependencies and resource availability before changing the host layout.

For a view that appears but lacks styling, inspect the project style resource and class assignments separately from import integrity. Record the first point where the imported example diverges from its documented contract. Retain the package revision and the local differences so a later upgrade can distinguish a packaging defect from a consumer customization.
## Separate package integrity, import and consumption

For the intended revision, inventory the resources actually supplied: view paths, descriptors, project scripts, named styles and any required stylesheet rules. Compare those paths with the development project. Two packages can contain resources with the same name while exposing different params. Resolve collisions before applying an update and preserve deliberate local modifications.

After import, test an unchanged previous consumer as well as a fresh example. The example verifies the new happy path; the existing consumer exercises omitted defaults, old params and previously customized styles. Capture the first failing boundary: archive, resource recognition in Designer, child rendering or host interaction. This makes a blank embed diagnosable without reinstalling unrelated components.

## Compare three resource versions

Use the previously installed upstream resource as the base, the current project resource as the local version and the proposed package as the incoming version. Compare each to the base. An incoming-only change can often be adopted directly. A local-only change identifies a customization to retain. When both sides changed a binding, style or parameter, inspect its consumer before combining them.

For example, the project may have customized the temperature unit while the package changed the binding supplying that field. Keeping the old label while taking the new binding can produce a unit mismatch. Reconcile label, conversion and binding together in a development copy. If the base revision is unavailable, record that limitation and compare against an actual consuming view. Preserve recoverable copies of replaced resources.

Deliver a short table of incoming path, local customization, chosen resolution and consumer used to validate it.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Styles duplicate on the second installation | Compare installed rule bodies, scopes and package revision. | Merge once and preserve customized declarations. |
| Import succeeds but the original host stops receiving outputs | Compare parameter directions and event names against the previous contract. | Repair the host mapping or document migration before replacing more views. |
