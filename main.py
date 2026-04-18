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
    sort_by_hilbert,
)


def sort_pixels(image_path: str, output_path: str, method: str):
    image = Image.open(image_path).convert("RGB")
    flat_rgb = np.array(image).reshape(-1, 3)
    flat_hsv = np.array(image.convert("HSV")).reshape(-1, 3)

    if method == "step":
        indices = sort_by_step(flat_rgb, flat_hsv)
    elif method == "hex":
        indices = sort_by_hex(flat_rgb)
    elif method == "luminosity":
        indices = sort_by_luminosity(flat_rgb)
    elif method == "saturation":
        indices = sort_by_saturation(flat_hsv)
    elif method in ("red-channel", "green-channel", "blue-channel"):
        channel = {"red-channel": 0, "green-channel": 1, "blue-channel": 2}[method]
        indices = sort_by_channel(flat_rgb, channel)

    sorted_pixels = flat_rgb[indices]

    h_img, w_img = image.size[1], image.size[0]
    result = Image.fromarray(sorted_pixels.reshape(h_img, w_img, 3).astype(np.uint8))
    result.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Path to image")
    parser.add_argument("--method", choices=["step", "hex", "luminosity", "saturation", "red-channel", "green-channel", "blue-channel", "hilbert"], default="step")
    args = parser.parse_args()

    p = Path(args.image)
    output_dir = Path("output") / p.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{args.method}_sorted_{p.name}"

    sort_pixels(args.image, str(output), args.method)
