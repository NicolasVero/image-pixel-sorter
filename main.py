from PIL import Image
import numpy as np


def sort_pixels(image_path: str, output_path: str):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image)

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            print(pixels[i , j])

if __name__ == "__main__":
    sort_pixels("input.jpg", "output.jpg")
