# Part 2 — Starter (Executable Spec)

No descriptive exercise text. The spec is the **golden transcript** in
`part2/tests/snapshot_interaction.txt`.

Students should implement:
- manual substring search counting overlapping occurrences (no `str.find`, no `in`, no regex),
- highlight spans and ANSI highlighting,
- printing only matching sonnets and the `N out of 3` line,
so that the app interaction matches the transcript exactly.

## Run the app

```bash
python -m part2.app
```

## Check against the transcript

```bash
python -m part2.tests.check_transcript
```

## Where to work

Edit `part2/app.py`:
- Implement `manual_count_occurrences`.
- Implement `find_spans` and verify highlighting matches the snapshot.
