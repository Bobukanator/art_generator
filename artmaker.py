# Module to randomly create cool images
# Brian Lawrence
# June 2022
from audioop import mul
import random
import math
from enum import IntEnum
from PIL import Image, ImageDraw

# Global Variables
MAX_PX_CANVAS = 512  # default
NUMBER_OF_GENERATED_IMAGES = 100  # default

CANVAS_SIZE = (MAX_PX_CANVAS, MAX_PX_CANVAS)
DRAW_PADDING = 15
BACKGROUND_COLOR = (255, 255, 255)


class DrawingBackgroundTechniques(IntEnum):
    """ INT Enum containing the different types of image.Draw techniques"""
    LINE = 1
    CHORD = 2
    PIESLICE = 3
    ELLIPSE = 4
    RECTANGLE = 5
    POLYGON = 6
    CONNECTEDLINES = 7


class DrawingForegroundTechniques(IntEnum):
    """ INT Enum containing the different types of image.Draw foreground techniques"""
    SQUIGGLES = 1
    BIGSQUIGGLES = 2
    SMALLSQUIGGLES = 3


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


def draw_random_background(image, color):
    """Creates a random background"""
    draw = ImageDraw.Draw(image)
    random_technique = random.randint(1, len(DrawingBackgroundTechniques))

    match random_technique:
        case DrawingBackgroundTechniques.LINE:
            draw.line((create_random_point(), create_random_point()), fill=color)
        case DrawingBackgroundTechniques.CHORD:
            draw.chord((create_random_point(), create_random_point()), create_random_angle(), create_random_angle(),
                       fill=color, outline=(0, 0, 0), width=1)
        case DrawingBackgroundTechniques.PIESLICE:
            draw.pieslice((create_random_point(), create_random_point()), create_random_angle(), create_random_angle(),
                          fill=color, outline=(0, 0, 0), width=1)
        case DrawingBackgroundTechniques.ELLIPSE:
            draw.ellipse(
                (create_random_point(), create_random_point()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingBackgroundTechniques.RECTANGLE:
            draw.rectangle(
                (create_random_point(), create_random_point()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingBackgroundTechniques.POLYGON:
            draw.polygon((create_random_point(), create_random_point(),
                         create_random_point()), fill=color, outline=(0, 0, 0), width=1)
        case DrawingBackgroundTechniques.CONNECTEDLINES:
            draw_random_connected_lines(draw, color)


def draw_random_foreground(image, color):
    """Creates a random foreground - the main worker function of this artmaker module"""
    draw = ImageDraw.Draw(image)
    random_technique = random.randint(1, len(DrawingForegroundTechniques))

    match random_technique:
        case DrawingForegroundTechniques.SQUIGGLES:
            draw_random_squiggles(draw, color)
        case DrawingForegroundTechniques.BIGSQUIGGLES:
            draw_random_bigsquiggle(draw, color)
        case DrawingForegroundTechniques.SMALLSQUIGGLES:
            draw_random_smallsquiggles(draw, color)


def draw_random_smallsquiggles(draw, color):
    """Uses points to create some squiggles - takes in draw,color"""
    point = create_random_point()
    for _ in range(random.randint(0, 500)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-1, 1), random.randint(-1, 1)))


def draw_random_squiggles(draw, color):
    """Uses points to create some squiggles - takes in draw,color"""
    point = create_random_point()
    for _ in range(random.randint(0, 2500)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-3, 3), random.randint(-3, 3)))


def draw_random_bigsquiggle(draw, color):
    """Uses points to create some big squiggles - takes in draw,color as"""
    point = create_random_point()
    for _ in range(random.randint(0, 5000)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-10, 10), random.randint(-10, 10)))


def add_points_together(point1, point2):
    """adding tuples is done this way - thanks Google!"""
    zipped = zip(point1, point2)
    mapped = map(sum, zipped)
    return tuple(mapped)


def draw_random_connected_lines(draw, color):
    """draw random connected lines"""
    point = create_random_point()
    for _ in range(random.randint(0, 50)):
        endpoint = create_random_point()
        draw.line((point, endpoint), fill=color)
        point = endpoint


def generate_image(maxoperations):
    """generate image and return - creating background first, followed by foreground """
    image = create_blank_canvas()
    for _ in range(random.randint(0, int(maxoperations/20))):
        draw_random_background(image, create_random_color())
    for _ in range(random.randint(0, maxoperations)):
        draw_random_foreground(image, create_random_color())
    return image
