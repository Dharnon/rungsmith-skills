# Two alarms with one display label

## Set up the case

Configure two simulated sources labelled High pressure. Give each a different source path. Filter the status table to the shared label.

## Exercise the interaction

Select B, reorder by priority, then inspect the selected event ID. A changed row index is expected. A changed selected event requires clearing or restoring selection before acknowledgment.

## Acceptance and evidence

Keep the two IDs and a record of the selected source after sorting. Replay separately with B already cleared.

## A journal event crosses a shift boundary

Use a simulated occurrence that activates shortly before the selected shift ends and clears just after. Inspect the event times and selected query interval. Ask whether the report promises transitions during the shift or conditions active during the shift. Those are different queries. Show the reviewer which records support each interpretation. Include the time zone, filter and EventId with the expected result.
