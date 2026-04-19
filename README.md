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

### `red-channel` / `green-channel` / `blue-channel`
Sorts by a single color channel. Produces unexpected graphical effects depending on the image.

```bash
python main.py photo.png --method red-channel
```

| red-channel | green-channel | blue-channel |
|-------------|---------------|--------------|
| ![red](https://github.com/user-attachments/assets/552fc3aa-c43f-4780-82bd-d2ff7d4dbf73) | ![green](https://github.com/user-attachments/assets/32045453-b3c0-4cf5-b174-00afef3a1229) | ![blue](https://github.com/user-attachments/assets/488b9108-e1ec-4588-8a59-3e45a82110d6) |

---

## Gallery 🖼️

<table>
  <tr>
    <td align="center"><b>Original</b></td>
    <td align="center"><b>Step</b></td>
    <td align="center"><b>Luminosity</b></td>
    <td align="center"><b>Hex</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/c2ccd261-dbbc-4edb-81e7-f07e5b4dcd28" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/ad5bad4e-dc2f-4a36-8008-4f521479b842" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/c402d214-73dd-406c-b8b1-1d7604512749" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/2e5ceb35-bbee-42f9-a092-dc4b80046d8b" width="200"/></td>
  </tr>
  <tr>
    <td align="center"><b>Saturation</b></td>
    <td align="center"><b>Red channel</b></td>
    <td align="center"><b>Green channel</b></td>
    <td align="center"><b>Blue Channel</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/634a3f9d-b653-48d5-8880-a5b12a7a52b4" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/0610b5a6-181e-470b-b634-5a70cda1a481" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/ba565857-363e-4996-834f-e3aafac3c894" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/577a4284-46e6-435b-b1c4-6e09dc11f188" width="200"/></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><b>Original</b></td>
    <td align="center"><b>Step</b></td>
    <td align="center"><b>Luminosity</b></td>
    <td align="center"><b>Hex</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/078c3f01-bdd2-433d-837b-2d7bd6739b9a" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/6c460449-9b38-42e5-b1c7-0f62c1027972" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/ab17b154-626d-4ab1-a210-4e68e931e680" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/ebcb7d44-9190-4ca4-a832-ac2496399e3b" width="200"/></td>
  </tr>
  <tr>
    <td align="center"><b>Saturation</b></td>
    <td align="center"><b>Red channel</b></td>
    <td align="center"><b>Green channel</b></td>
    <td align="center"><b>Blue Channel</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2bf20a1a-33e8-402e-ac9a-be58bab245ca" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/55c42d4f-cdc3-451e-b54d-0626aab43358" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/b9aa8ebf-bb7f-496a-891c-2d19cf5ebdcc" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/e18f4fd9-02b9-4eaa-8b54-4a5db8f424cc" width="200"/></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><b>Original</b></td>
    <td align="center"><b>Step</b></td>
    <td align="center"><b>Luminosity</b></td>
    <td align="center"><b>Hex</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/eebff316-4d59-4544-bf0d-a0b4cbcb5e99" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/7194599b-5cb0-4163-a9bd-3fc9df672dab" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/6bfcbfa4-536b-427e-8f79-a914116f2b56" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/ef8d0fed-ba77-48c5-99eb-e24c8d9e3bdf" width="200"/></td>
  </tr>
  <tr>
    <td align="center"><b>Saturation</b></td>
    <td align="center"><b>Red channel</b></td>
    <td align="center"><b>Green channel</b></td>
    <td align="center"><b>Blue Channel</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/ca11dae0-1485-4a92-b7d5-d6e9e1fbd38b" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/0e7e6e64-b71e-4a66-986b-68ad750f896e" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/64467ab3-352b-4ac5-86fc-b80f6bfe6f4e" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/f420e86a-c5b2-447b-a796-1eb0bac090ca" width="200"/></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><b>Original</b></td>
    <td align="center"><b>Step</b></td>
    <td align="center"><b>Luminosity</b></td>
    <td align="center"><b>Hex</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/7dcfd44a-847e-4f1d-8775-08a082add4ea" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/94a5115e-2e6a-4692-a0f9-85cfdcb97457" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/de0c64da-6b52-42a4-8b76-dfa567a3105e" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/e0bada9d-e4f8-4846-b969-343a6d8b202a" width="200"/></td>
  </tr>
  <tr>
    <td align="center"><b>Saturation</b></td>
    <td align="center"><b>Red channel</b></td>
    <td align="center"><b>Green channel</b></td>
    <td align="center"><b>Blue Channel</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/e5ad23da-d540-479d-9867-9dcb436e2732" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/0df26e6d-517e-421c-8bdb-f21664f6966e" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/4be7b42d-4a3c-43d5-974c-39314f11007b" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/b8b1aad9-6c8c-48cc-8140-931c8145dfb8" width="200"/></td>
  </tr>
</table>

--- 
## Credits💡

The `step` sorting algorithm is based on [Improving the Rainbow – Luma Correction](https://www.alanzucconi.com/2015/09/30/colour-sorting/) by Alan Zucconi.
