#!/usr/bin/env python3
"""Create a non-overlapping <=100 px tile manifest for an image region."""

import argparse
import csv
from pathlib import Path


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be positive")
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--x0", type=int, required=True)
    parser.add_argument("--y0", type=int, required=True)
    parser.add_argument("--width", type=positive_int, required=True)
    parser.add_argument("--height", type=positive_int, required=True)
    parser.add_argument("--tile-size", type=positive_int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.x0 < 0 or args.y0 < 0:
        raise SystemExit("x0 and y0 must be non-negative")
    if args.tile_size > 100:
        raise SystemExit("tile-size must be between 1 and 100")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "tile_id", "tile_row", "tile_col", "x0", "y0", "width", "height",
        "count", "confidence", "ambiguous_count", "excluded_notes",
    ]
    rows = (args.height + args.tile_size - 1) // args.tile_size
    cols = (args.width + args.tile_size - 1) // args.tile_size

    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        tile_id = 0
        for row in range(rows):
            for col in range(cols):
                x = args.x0 + col * args.tile_size
                y = args.y0 + row * args.tile_size
                writer.writerow({
                    "tile_id": f"T{tile_id:04d}",
                    "tile_row": row,
                    "tile_col": col,
                    "x0": x,
                    "y0": y,
                    "width": min(args.tile_size, args.x0 + args.width - x),
                    "height": min(args.tile_size, args.y0 + args.height - y),
                    "count": "",
                    "confidence": "",
                    "ambiguous_count": "",
                    "excluded_notes": "",
                })
                tile_id += 1


if __name__ == "__main__":
    main()

