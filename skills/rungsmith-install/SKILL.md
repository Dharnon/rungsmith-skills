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
3. Preserve existing project files. Import the package into the requested development project with native resource descriptors and paths intact. Append required styles; do not replace the project stylesheet. Embed with ia.display.view and the returned props.path and props.params. Handle duplicate view paths before replacing anything.
4. Wire outputs and process commands in the owner view according to the actual contract. Sample controls are not evidence of PLC integration. Do not perform tag writes or operate equipment without the user's authorization.
5. Validate JSON and references, then test in a native Perspective client. Report package integrity, Designer import and runtime verification separately. For an update, compare the old and new contract and preserve local customizations; never overwrite a customized package merely because a newer version exists.

Without MCP, use /api/catalog/{id}?format=markdown on https://www.rungsmith.dev and follow its actual download link. Do not invent an npm or shadcn installer for Perspective. MCP retrieval is read-only; use authorized local tools to make changes.
