from PIL import Image, ImageDraw
import random

# Global Variables
max_px_canvas = 128
canvas_size = (max_px_canvas, max_px_canvas)
draw_padding = 15
background_color = (255, 255, 255)
imagename = "TestImage.png"
directory = "art_generator/images/"
# color palette
main_color = (33, 255, 33)


def createBlankCanvas():
    image = Image.new("RGB", canvas_size, background_color)
    return image


def createRandomColor():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    return (R, G, B)


def createRandomPoint():
    return (
        random.randint(0+draw_padding, max_px_canvas-draw_padding),
        random.randint(0+draw_padding, max_px_canvas-draw_padding)
    )


def createRandomAngle():
    return random.randint(0, 360)


def createRandomPoints(image, pointCount):
    draw = ImageDraw.Draw(image)
    pt_color = main_color

    for _ in range(pointCount):
        randomPoint = (
            random.randint(0+draw_padding, max_px_canvas-draw_padding),
            random.randint(0+draw_padding, max_px_canvas-draw_padding)
        )
        draw.point(randomPoint, fill=createRandomColor())


def createRandomFlowerWithColor(image, locationPt, petalCount, color):
    draw = ImageDraw.Draw(image)

    for _ in range(petalCount):
        random_lineend = (
            random.randint(0+draw_padding, max_px_canvas-draw_padding),
            random.randint(0+draw_padding, max_px_canvas-draw_padding)
        )

        draw.chord((locationPt, random_lineend), createRandomAngle(), createRandomAngle(),
                   fill=color, outline=(0, 0, 0), width=1)


def createRandomLines(image, lineCount):
    draw = ImageDraw.Draw(image)

    for _ in range(lineCount):
        random_linestart = (
            random.randint(0+draw_padding, max_px_canvas-draw_padding),
            random.randint(0+draw_padding, max_px_canvas-draw_padding)
        )
        random_lineend = (
            random.randint(0+draw_padding, max_px_canvas-draw_padding),
            random.randint(0+draw_padding, max_px_canvas-draw_padding)
        )

        line_xy = (random_linestart, random_lineend)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill=line_color)


def generateBasic():

    image = createBlankCanvas()
    createRandomPoints(image, 400)
    for _ in range(10):
        createRandomFlowerWithColor(
            image, createRandomPoint(), 5, createRandomColor())
    image.save(directory+imagename)


if __name__ == "__main__":
    generateBasic()
