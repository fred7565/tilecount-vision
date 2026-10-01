---
name: tilecount-vision
description: Count spots, cells, puncta, or other image objects inside a specified region by splitting it into non-overlapping tiles no larger than 100x100 pixels, recording auditable per-tile results, and reporting deduplicated totals. Use when whole-image counting is unreliable or the user needs clear-versus-dim counts and evidence files.
---

# TileCount Vision

Count image objects inside an exact region with an auditable tile-by-tile workflow.

## Workflow

1. Confirm the source image's pixel dimensions and the analysis rectangle `(x0, y0, width, height)`. If coordinates are inferred from a visual selection, state the inference and confidence.
2. Run `scripts/make_tile_manifest.py` to partition only that rectangle. Each tile must be at most 100x100 pixels, and tiles must never overlap.
3. Inspect every tile at original resolution. Count only the requested object class and explicitly exclude stated negatives such as fibers, mesh, diffuse background, merged texture, or non-target colors.
4. Assign each object to the tile containing its center. Context outside a tile may help classification but must never create an additional count.
5. Record every tile in CSV. Include coordinates, count, confidence, ambiguous candidates, and excluded structures.
6. Sum accepted objects exactly once and write a JSON summary. Report the region, tile count, total, ambiguity, and evidence paths.

## Clear and dim mode

When the user requests separate certainty levels:

- `clear_count`: compact, locally bright, color-consistent objects that are confidently distinct from background.
- `dim_additional_count`: plausible but weaker objects not already present in `clear_count`.
- `inclusive_total = clear_count + dim_additional_count`.

Never count the same center in both categories. Keep ambiguous candidates separate when evidence is insufficient.

## Quality rules

- Do not estimate the total by extrapolating from sample tiles.
- Reject elongated continuous fibers and reticular texture unless the user explicitly targets them.
- Use object centers for boundary assignment. If the center cannot be determined, mark it ambiguous instead of silently choosing a tile.
- Prefer an annotated contact sheet when practical so users can audit misses and false positives.
- State uncertainty honestly; do not present a false exact count for visually unresolved tiles.

Read [references/output-schema.md](references/output-schema.md) before writing results.

