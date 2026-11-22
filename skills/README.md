# Rungsmith skills for Ignition Perspective

Install the selected workflows with the open skills CLI (Node.js required):

```sh
npx skills add Dharnon/rungsmith-skills
```

Install one workflow for Codex:

```sh
npx skills add Dharnon/rungsmith-skills --skill rungsmith-perspective-css -a codex
```

Add `-g` for all projects. `npx skills update` checks installed skills for updates. The same instructions work with Free and Pro; resource access still follows the user's plan. These are instructions for an agent, not Ignition module or component installers.

## Choose the right Perspective entry point

- [rungsmith-perspective](rungsmith-perspective/SKILL.md): discover, inspect, validate and obtain **registered** Rungsmith component resources and packages through the read-only catalog.
- [rungsmith-perspective-engineering](rungsmith-perspective-engineering/SKILL.md): **build or review real native views**, view parameters, bindings, instance identity, operator states and import/runtime evidence; works without a catalog component.
- [rungsmith-ask-rungsmith](rungsmith-ask-rungsmith/SKILL.md): route an unclear UI symptom or broad request to the narrowest workflow.

The engineering skill contains [four reproducible fixture recipes](rungsmith-perspective-engineering/RECIPES.md) and [nine evaluation prompts](rungsmith-perspective-engineering/EVALS.md). These are instructional acceptance tests, not a claim of tested imports. Run the same fixtures against an authorized development Gateway before marking them native-verified.

## Readiness

The three existing workflows are available. New preview and draft workflows are published for review, with native verification pending. Read each guide and review changes before relying on it in a plant. Installation never grants permission to operate equipment or write tags.

Compare the 35 guides and see which practical gap each revision addresses in the [skill comparison](COMPARISON.md).

## Documentation

Browse the guides at [rungsmith.dev/skills](https://www.rungsmith.dev/skills). This repository contains agent instructions and supporting references only; it does not distribute Premium component source.
