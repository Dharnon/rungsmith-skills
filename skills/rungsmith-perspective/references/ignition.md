# Use the right source

Use `search_docs` for layout, embedding or event questions; use `get_doc` to read the selected guide. Responses include Ignition version, review date, official links, local provenance and examples. This is a curated subset, not the entire manual or live web search.

Prefer the installed component's actual contract for Viewcraft params. Prefer official version-matched Ignition documentation for platform APIs. Local conventions are design guidance, not proof of the platform schema. If they conflict, state the conflict and verify before generating files.

Corrections verified for 8.3:

- Flex children use `position.grow`, `position.shrink`, `position.basis`. `props.wrap` is `nowrap`, `wrap` or `wrap-reverse`.
- Embedded Views use `props.path` and matching `props.params`.
- `system.perspective.openPopup` requires both the popup ID and view path. A dict as its second positional argument is not a replacement for the view path.
- `system.perspective.sendMessage` targets component message handlers, not Session Event message handlers. Check scope and instance identity.

Do not turn unverified local snippets into universal rules. Keep source validation, Designer import and native runtime verification distinct. Follow the official links returned by the guide when more detail is required.
