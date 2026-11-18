# Native composition

- Start from the actual view.json returned by the registry. Its view.params plus propConfig define the reusable contract; component props inside root are not interchangeable with view parameters.
- Use an Embedded View (`ia.display.view`) at the exact returned view path. A minimal props shape is `{ "path": "Primitives/Button", "params": { "label": "Confirmar", "variant": "outline" } }`. Use this example only if the selected contract contains those inputs.
- Parent Flex layout controls grow, shrink and basis. Small controls need bounded widths; avoid making number inputs span the entire page. Verify the host container as well as the embedded view at narrow widths.
- Preserve `resource.json` with its view, the required named styles, and event handlers. Shared stylesheet requirements must be resolved before claiming visual parity. Do not replace the host's complete stylesheet with a component snippet.
- Avoid importing or overwriting an entire project to add one control. Inspect existing resources and resolve conflicts deliberately in the user's development project.
- Native Jython/Perspective event scripts are not browser JavaScript. A configured message name needs its receiver in the host view; it is not a functioning plant action on its own.
- After filesystem edits, follow the target Gateway's documented refresh workflow. Ignition 8.3 may need Scan File System. No scan or Designer import is performed by the free MCP.
- Synthetic examples remain synthetic until the user explicitly supplies and authorizes real tag/query bindings.
