from PIL import Image, ImageDraw
from enum import IntEnum
import random

# Global Variables
max_px_canvas = 256
number_of_generated_images = 1000

canvas_size = (max_px_canvas, max_px_canvas)
draw_padding = 15
background_color = (255, 255, 255)
directory = "images/"


# INT Enum containing the different types of image.Draw techniques
#
#
class DrawingTechniques(IntEnum):
    LINE = 1
    CHORD = 2
    PIESLICE = 3
    ELLIPSE = 4
    RECTANGLE = 5
    POLYGON = 6


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


def DrawARandomTechnique(image, color):
    draw = ImageDraw.Draw(image)
    RandomTechnique = random.randint(1, len(DrawingTechniques))

    match RandomTechnique:
        case DrawingTechniques.LINE:
            draw.line((createRandomPoint(), createRandomPoint()), fill=color)
        case DrawingTechniques.CHORD:
            draw.chord((createRandomPoint(), createRandomPoint()), createRandomAngle(), createRandomAngle(),
                       fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.PIESLICE:
            draw.pieslice((createRandomPoint(), createRandomPoint()), createRandomAngle(), createRandomAngle(),
                          fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.ELLIPSE:
            draw.ellipse(
                (createRandomPoint(), createRandomPoint()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.RECTANGLE:
            draw.rectangle(
                (createRandomPoint(), createRandomPoint()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.POLYGON:
            draw.polygon((createRandomPoint(), createRandomPoint(),
                         createRandomPoint()), fill=color, outline=(0, 0, 0), width=1)


def generateBasic(imagename):

    image = createBlankCanvas()
    for _ in range(random.randint(0, 100)):
        DrawARandomTechnique(image, createRandomColor())

    image.save(directory+imagename)


if __name__ == "__main__":
    print("This program generates random images.. starting now!")
    for i in range(number_of_generated_images):
        imagename = "genImage"+str(i+1)+".png"
        generateBasic(imagename)
        print(imagename + " generated.")
