---
name: rungsmith-learn-project-taste
description: "Repeated design corrections across sessions. A short, reviewable rule set grounded in the actual corrections."
metadata:
  status: draft
  native-verification: pending
---

# Learn project taste

A short, reviewable rule set grounded in the actual corrections.

Practice this workflow in a development project: [Turn a density correction into a scoped rule](RECIPES.md).

## Workflow

1. Extract confirmed corrections from the session and the diff; separate user decisions from inferred reasons.

2. Turn each correction into a scoped rule with an example and rationale.

3. Propose additions or pruning to DESIGN.md; do not invent preferences or silently generalize one screen.

## Determine the scope of a design correction

If a reviewer asks for denser rows on a historian screen, inspect the changed table, its style class and other consumers. Check whether the correction was about comparing timestamps, fitting a workstation viewport or a broader site standard. Quote the actual decision and label any inferred rationale.

Draft a rule with the task, affected resource family, observable change and an exception backed by project evidence. For example, compact history rows may aid comparison while a touch-operated equipment picker needs its existing hit targets. Look for an existing rule that can be clarified before adding one. Present the proposed wording and supporting paths for review.

## Resolve contradictory feedback across screens

Keep the task context attached to each correction. An operator asking for persistent labels on a control faceplate and a maintainer asking for compact icon actions on a historical table can both be describing good local decisions. Inspect frequency of use, equipment context and target input device before merging them into a project convention.

Write a candidate rule against a pair of existing views and predict which one it would change. If it alters a view the reviewer intentionally approved, narrow the rule or preserve the two conventions separately. Keep inferred rationale labelled until confirmed. When a later correction supersedes a rule, revise the old wording and its example so both versions do not continue guiding future changes.

## Decide whether a correction belongs in project guidance

Capture the original request, the resulting diff and the surface where the reviewer approved it. Look for an existing convention that already explains the correction. A request to simplify one sensor panel may be a local information-density issue. Two repeated corrections across unrelated projects still need evidence before becoming a site-wide HMI rule.

Write a candidate rule with a recognizable trigger, a concrete action and a limiting case. “Keep the equipment identifier visible while detail tabs change” is testable on a real view. “Make it feel industrial” leaves future agents free to invent conflicting changes. Keep a citation to the project path or review decision that lets a maintainer revisit the rule.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Two reviewers prefer opposite densities | Compare target device, task and resource family for each approved decision. | Keep scoped conventions with examples where each applies. |
| A proposed rule merely restates a preference adjective | Ask what would change in an existing view and what observable result would improve. | Capture that actionable change or keep the observation provisional. |

## Evidence and handoff

A short, reviewable rule set grounded in the actual corrections. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

Review our corrections to spacing, semantic colors and disabled states. Propose reusable rules with their evidence.
