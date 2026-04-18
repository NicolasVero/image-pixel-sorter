from PIL import Image
from pathlib import Path
import numpy as np
import argparse


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


def sort_by_step(flat_rgb, flat_hsv, repetitions: int = 8):
    r, g, b = normalize(flat_rgb).T
    lum = np.sqrt(0.241 * r + 0.691 * g + 0.068 * b)
    h, s, v = normalize(flat_hsv).T

    h2 = (h * repetitions).astype(int)
    v2 = (v * repetitions)

    odd = (h2 % 2 == 1)
    lum2 = np.where(odd, repetitions - lum, lum)
    v3 = np.where(odd, repetitions - v2, v2)

    is_neutral = (s < 0.15).astype(int)

    return np.lexsort((v3, lum2, h2, is_neutral))


def sort_by_hex(flat_rgb):
    flat = flat_rgb.astype(np.int32)
    hex_values = flat[:,0]*65536 + flat[:,1]*256 + flat[:,2]
    return np.argsort(hex_values)


def sort_by_luminosity(flat_rgb):
    r, g, b = normalize(flat_rgb).T
    lum = np.sqrt(0.299 * r + 0.587 * g + 0.114 * b)
    return np.argsort(lum)


def sort_by_saturation(flat_hsv):
    h, s, v = normalize(flat_hsv).T
    return np.argsort(s)


def sort_by_channel(flat_rgb, channel: int):
    return np.argsort(flat_rgb[:, channel])


def normalize(flat):
    return flat / 255.0


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
