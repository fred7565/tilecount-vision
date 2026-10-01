# Output schema

## Per-tile CSV

Required columns:

```text
tile_id,tile_row,tile_col,x0,y0,width,height,count,confidence,ambiguous_count,excluded_notes
```

For separate certainty levels, use:

```text
tile_id,tile_row,tile_col,x0,y0,width,height,clear_count,dim_additional_count,inclusive_total,confidence,ambiguous_count,excluded_notes
```

Coordinates use the source image's pixel system with origin `(0, 0)` at the top-left. `x0` and `y0` are inclusive. `count` is the number of accepted object centers assigned to that tile.

## Summary JSON

```json
{
  "source_image": "...",
  "region": {"x0": 0, "y0": 0, "width": 0, "height": 0},
  "tile_size": {"max_width": 100, "max_height": 100},
  "tile_count": 0,
  "total_count": 0,
  "ambiguous_count": 0,
  "per_tile_csv": "...",
  "notes": "..."
}
```

When clear/dim mode is used, replace `total_count` with `clear_count`, `dim_additional_count`, and `inclusive_total`.

