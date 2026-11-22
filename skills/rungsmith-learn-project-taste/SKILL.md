---
name: rungsmith-learn-project-taste
description: "Repeated design corrections across sessions. A short, reviewable rule set grounded in the actual corrections."
metadata:
  status: draft
  native-verification: pending
---

# Learn project taste

A short, reviewable rule set grounded in the actual corrections.

## Workflow

1. Extract confirmed corrections from the session and the diff; separate user decisions from inferred reasons.

2. Turn each correction into a scoped rule with an example and rationale.

3. Propose additions or pruning to DESIGN.md; do not invent preferences or silently generalize one screen.

## Determine the scope of a design correction

If a reviewer asks for denser rows on a historian screen, inspect the changed table, its style class and other consumers. Check whether the correction was about comparing timestamps, fitting a workstation viewport or a broader site standard. Quote the actual decision and label any inferred rationale.

Draft a rule with the task, affected resource family, observable change and an exception backed by project evidence. For example, compact history rows may aid comparison while a touch-operated equipment picker needs its existing hit targets. Look for an existing rule that can be clarified before adding one. Present the proposed wording and supporting paths for review.

## Evidence and handoff

A short, reviewable rule set grounded in the actual corrections. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

Review our corrections to spacing, semantic colors and disabled states. Propose reusable rules with their evidence.
