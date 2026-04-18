from PIL import Image
import numpy as np
import argparse


def sort_pixels(image_path: str, output_path: str, method: str):
    image = Image.open(image_path).convert("RGB")
    flat_rgb = np.array(image).reshape(-1, 3)
    flat_hsv = np.array(image.convert("HSV")).reshape(-1, 3)

    indices = sort_by_step(flat_rgb, flat_hsv)
    sorted_pixels = flat_rgb[indices]

    h_img, w_img = image.size[1], image.size[0]
    result = Image.fromarray(sorted_pixels.reshape(h_img, w_img, 3).astype(np.uint8))
    result.save(output_path)

def sort_by_step(flat_rgb, flat_hsv, repetitions: int = 8):
    r = flat_rgb[:, 0] / 255.0
    g = flat_rgb[:, 1] / 255.0
    b = flat_rgb[:, 2] / 255.0

    lum = np.sqrt(0.241 * r + 0.691 * g + 0.068 * b)

    h = flat_hsv[:, 0] / 255.0
    s = flat_hsv[:, 1] / 255.0
    v = flat_hsv[:, 2] / 255.0

    h2 = (h * repetitions).astype(int)
    v2 = (v * repetitions)

    odd = (h2 % 2 == 1)
    lum2 = np.where(odd, repetitions - lum, lum)
    v3 = np.where(odd, repetitions - v2, v2)

    is_neutral = (s < 0.15).astype(int)

    return np.lexsort((v3, lum2, h2, is_neutral))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Path to image")
    parser.add_argument("--method", choices=["step", "hex"], default="step")
    args = parser.parse_args()

    sort_pixels(args.image, "sorted_" + args.image, args.method)
