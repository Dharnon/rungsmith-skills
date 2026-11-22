# Distinguish an aggregated excursion from a missing interval

## Set up the case

Use fixture history with a short high excursion followed by a known sample gap. Select a narrow window that contains both, then widen the range.

## Exercise the interaction

Compare axis bounds, returned timestamps and aggregation settings. If a spike disappears, inspect the query result before changing chart smoothing. If a line bridges the missing interval, inspect series gap handling.

## Acceptance and evidence

Record the exact window, time zone and sample treatment, then switch assets while the earlier query is pending.

## Check a clock change with two similar local labels

Use a fixture interval spanning a repeated local hour when relevant to the deployment. Supply distinct timestamps and values for the two occurrences. Inspect query bounds, ordering, axis labels and tooltip detail. Confirm a reviewer can identify which sample came first. Retain the time zone and precise timestamps with the reproduction.
