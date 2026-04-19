# Image pixel sorter

Sort every pixel of an image by color, using different sorting algorithms.

---

## Installation 📦

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage 🖥️

```bash
python main.py <image> --method <method>
```

The output is saved in `output/<image>/`.

**Original image:**

![original](https://github.com/user-attachments/assets/ce1e94f8-fe5c-4487-a105-4a42d8e25f4e)

---

## Methods 🎨

| Method | Effect |
|--------|--------|
| `hex` | Dark to light via raw RGB spectrum |
| `luminosity` | Dark to light, perceptually weighted |
| `step` | Smooth rainbow spectrum with zigzag transitions |
| `saturation` | From grey to most colorful |
| `red-channel` / `green-channel` / `blue-channel` | Graphical effects by single channel |
| `all` *(default method)* | Runs all methods and saves each result |

### `hex`
Sorts by raw RGB hex value `R × 65536 + G × 256 + B`. Simple but produces sharp transitions.

```bash
python main.py photo.png --method hex
```
![hex](https://github.com/user-attachments/assets/d2fa9358-290a-4d64-aff7-f3ec019688d7)

---

### `luminosity`
Sorts by perceived brightness from darkest to lightest.

```bash
python main.py photo.png --method luminosity
```
![luminosity](https://github.com/user-attachments/assets/24a9f8bd-c898-4c17-aa63-6a729a393b63)

---

### `step`
Sorts by hue using a zigzag pattern to create smooth transitions between color segments. Neutral colors (grey, black, white) are grouped at the end.

```bash
python main.py photo.png --method step
```
![step](https://github.com/user-attachments/assets/460e55cb-d9f9-4d20-9834-31c30bc58662)

---

### `saturation`
Sorts from least to most colorful — greys first, vivid colors last.

```bash
python main.py photo.png --method saturation
```
![saturation](https://github.com/user-attachments/assets/22643546-8295-44f0-955e-9a14296fd47e)

---



---

### `red-channel` / `green-channel` / `blue-channel`
Sorts by a single color channel. Produces unexpected graphical effects depending on the image.

```bash
python main.py photo.png --method red-channel
```

| red-channel | green-channel | blue-channel |
|-------------|---------------|--------------|
| ![red](https://github.com/user-attachments/assets/552fc3aa-c43f-4780-82bd-d2ff7d4dbf73) | ![green](https://github.com/user-attachments/assets/32045453-b3c0-4cf5-b174-00afef3a1229) | ![blue](https://github.com/user-attachments/assets/488b9108-e1ec-4588-8a59-3e45a82110d6) |

--- 
## Credits💡

The `step` sorting algorithm is based on [Improving the Rainbow – Luma Correction](https://www.alanzucconi.com/2015/09/30/colour-sorting/) by Alan Zucconi.
