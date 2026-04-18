import numpy as np


def normalize(flat):
    return flat / 255.0


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
    hex_values = flat[:, 0] * 65536 + flat[:, 1] * 256 + flat[:, 2]
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
