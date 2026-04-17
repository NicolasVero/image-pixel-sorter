from PIL import Image
import numpy as np


def sort_pixels(image_path: str, output_path: str):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image)

    flat = pixels.reshape(-1, 3).astype(np.int32)
    hex_values = flat[:,0]*65536 + flat[:,1]*256 + flat[:,2]
    indices = np.argsort(hex_values)

    sorted_pixels = flat[indices]
    h, w, _ = image.size[1], image.size[0], 3
    sorted_pixels = sorted_pixels.reshape(h, w, 3)

    result = Image.fromarray(sorted_pixels.astype(np.uint8))
    result.save(output_path)   

if __name__ == "__main__":
    sort_pixels("input.jpg", "output.jpg")
