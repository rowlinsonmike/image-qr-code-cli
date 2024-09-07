<h1 align="center">
  <br>
  <img src="docs/example.png" alt="image qr code cli" width="400"/>
  <br>
  Image QR Code Generator CLI
  <br>
</h1>

<h4 align="center">a simple cli that creates a qr code from an existing image</h4>

<p align="center">
  <a href="#how-it-works">How it Works</a> •
  <a href="#install">Install</a> •
  <a href="#how-to-use">How to Use</a> •
</p>

## How it Works

This CLI takes a specified image, darkens it based on how bright the image is, and uses a generated qr code as a mask for the image itself.

You can override the brightness if the QR code doesn't scan well. Setting the brightness switch closer to 1 from 100 darkens the image.

The CLI will output a `qr_code.png` image in the current working directory.

## Install

```bash
pip install https://github.com/rowlinsonmike/image-qr-code-cli/blob/main/dist/imgqr-0.1.0.tar.gz
```

## How to use

### Available CLI Commands

```

╭─ Commands ───────────────────────────────────────────────────────────────────╮                                                                         │
│ run    generate qr code from image                                           │
╰──────────────────────────────────────────────────────────────────────────────╯

```

### Run command

```
 Usage: imgqr run [OPTIONS] URL IMAGE

 generate qr code with image

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    url        TEXT  url [default: None] [required]                         │
│ *    image      TEXT  local image path [default: None] [required]            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --brightness        INTEGER RANGE [1<=x<=100]  An optional switch with a     │
│                                                value between 1 and 100       │
│                                                [default: 70]                 │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Example

```bash
imgqr run --brightness 70 'google.com' 'my_image.png'
```
