# Module to randomly create cool images
# Brian Lawrence
# June 2022
import random
from enum import IntEnum
from PIL import Image, ImageDraw

# Global Variables
MAX_PX_CANVAS = 512  # default
NUMBER_OF_GENERATED_IMAGES = 100  # default

CANVAS_SIZE = (MAX_PX_CANVAS, MAX_PX_CANVAS)
DRAW_PADDING = 15
BACKGROUND_COLOR = (255, 255, 255)


class DrawingTechniques(IntEnum):
    """ INT Enum containing the different types of image.Draw techniques"""
    LINE = 1
    CHORD = 2
    PIESLICE = 3
    ELLIPSE = 4
    RECTANGLE = 5
    POLYGON = 6


def create_blank_canvas():
    """creates new image blank canvas"""
    image = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)
    return image


def create_random_color():
    """returns random RGB color"""
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    return (R, G, B)


def create_random_point():
    """returns 2 random points within the bounds of the drawing canvas"""
    return (
        random.randint(0+DRAW_PADDING, MAX_PX_CANVAS-DRAW_PADDING),
        random.randint(0+DRAW_PADDING, MAX_PX_CANVAS-DRAW_PADDING)
    )


def create_random_angle():
    """returns random image from 0 to 360 degrees"""
    return random.randint(0, 360)


def draw_random_technique(image, color):
    """Creates a random picture - the main worker function of this artmaker module"""
    draw = ImageDraw.Draw(image)
    RandomTechnique = random.randint(1, len(DrawingTechniques))

    match RandomTechnique:
        case DrawingTechniques.LINE:
            draw.line((create_random_point(), create_random_point()), fill=color)
        case DrawingTechniques.CHORD:
            draw.chord((create_random_point(), create_random_point()), create_random_angle(), create_random_angle(),
                       fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.PIESLICE:
            draw.pieslice((create_random_point(), create_random_point()), create_random_angle(), create_random_angle(),
                          fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.ELLIPSE:
            draw.ellipse(
                (create_random_point(), create_random_point()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.RECTANGLE:
            draw.rectangle(
                (create_random_point(), create_random_point()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingTechniques.POLYGON:
            draw.polygon((create_random_point(), create_random_point(),
                         create_random_point()), fill=color, outline=(0, 0, 0), width=1)


def generate_image(maxoperations):
    """generate image and return """
    image = create_blank_canvas()
    for _ in range(random.randint(0, maxoperations)):
        draw_random_technique(image, create_random_color())
    return image
