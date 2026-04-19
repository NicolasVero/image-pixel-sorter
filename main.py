from PIL import Image
from pathlib import Path
import numpy as np
import argparse

from sorting import (
    sort_by_step,
    sort_by_hex,
    sort_by_luminosity,
    sort_by_saturation,
    sort_by_channel,
)


METHODS = {
    "step":          lambda rgb, hsv: sort_by_step(rgb, hsv),
    "hex":           lambda rgb, hsv: sort_by_hex(rgb),
    "luminosity":    lambda rgb, hsv: sort_by_luminosity(rgb),
    "saturation":    lambda rgb, hsv: sort_by_saturation(hsv),
    "red-channel":   lambda rgb, hsv: sort_by_channel(rgb, 0),
    "green-channel": lambda rgb, hsv: sort_by_channel(rgb, 1),
    "blue-channel":  lambda rgb, hsv: sort_by_channel(rgb, 2),
}


def sort_pixels(image_path: str, output_path: str, method: str):
    image = Image.open(image_path).convert("RGB")
    flat_rgb = np.array(image).reshape(-1, 3)
    flat_hsv = np.array(image.convert("HSV")).reshape(-1, 3)

    indices = METHODS[method](flat_rgb, flat_hsv)

    sorted_pixels = flat_rgb[indices]

    h_img, w_img = image.size[1], image.size[0]
    result = Image.fromarray(sorted_pixels.reshape(h_img, w_img, 3).astype(np.uint8))
    result.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Path to image")
    parser.add_argument("--method", choices=[*METHODS.keys(), "all"], default="all")
    args = parser.parse_args()

    p = Path(args.image)
    if not p.exists():
        print(f"Error: file '{p}' not found.")
        exit(1)

    output_dir = Path("output") / p.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    methods = METHODS.keys() if args.method == "all" else [args.method]
    for method in methods:
        output = output_dir / f"{method}_sorted_{p.name}"
        sort_pixels(args.image, str(output), method)
