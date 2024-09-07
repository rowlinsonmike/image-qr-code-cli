import qrcode
from PIL import Image, ImageEnhance, ImageStat
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
import typer
from typing_extensions import Annotated


def darken_image(image_path, target_brightness=100, step=0.05):
    # open image
    img = Image.open(image_path)

    # calc average brightness
    def get_average_brightness(image):
        grayscale_image = image.convert("L")
        stat = ImageStat.Stat(grayscale_image)
        return stat.mean[0]

    # get initial brightness
    current_brightness = get_average_brightness(img)
    # create brightness enhancer
    enhancer = ImageEnhance.Brightness(img)
    # darken the image to target brightness
    factor = 1.0
    while current_brightness > target_brightness:
        factor -= step
        darkened_img = enhancer.enhance(factor)
        current_brightness = get_average_brightness(darkened_img)
    # return image
    return darkened_img


def create_qr(data, image_path, brightness, output_path):
    # open main image
    main_image = darken_image(image_path, brightness)
    # create qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    # add url to qr code
    qr.add_data(data)
    qr.make(fit=True)
    # create image from qr code
    mask_image = qr.make_image(
        fill_color="white",
        back_color="black",
    )
    # make mask grayscale
    mask_image = mask_image.convert("L")
    # resize image to qr code size
    if mask_image.size != main_image.size:
        main_image = main_image.resize(mask_image.size)

    # create image with alpha channel
    result = Image.new("RGBA", main_image.size)
    # page main image using mask (qr code)
    result.paste(main_image, (0, 0), mask_image)
    # save generated image
    result.save(output_path)


app = typer.Typer()


@app.command("main")
def run_main():
    print(f"simple image qr code cli")


@app.command("run")
def run_command(
    url: Annotated[str, typer.Argument(help="url")],
    image: Annotated[str, typer.Argument(help="local image path")],
    brightness: int = typer.Option(
        default=70,
        min=1,
        max=100,
        clamp=True,
        help="An optional switch with a value between 1 and 100",
    ),
):
    """
    generate qr code with image
    """
    create_qr(url, image, brightness, "qr_code.png")


if __name__ == "__main__":
    app()
