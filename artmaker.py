""" Module to randomly create cool images
    Brian Lawrence
    June 2022 """
import random
import math
from enum import IntEnum
import numpy as np
import matplotlib.cm
from PIL import Image, ImageDraw, ImageFilter

# Global Variables
MAX_PX_CANVAS = 512  # default
MAX_SIZE_SHAPE = 250  # used to determine how big a shape is

CANVAS_SIZE = (MAX_PX_CANVAS, MAX_PX_CANVAS)
DRAW_PADDING = 15
BACKGROUND_COLOR = (255, 255, 255)


class DrawingShapeTechniques(IntEnum):
    """ INT Enum containing the different types of image.Draw techniques"""
    LINE = 1
    CONNECTEDLINES = 2
    RECTANGLE = 3
    POLYGON = 4
    CHORD = 5
    PIESLICE = 6
    ELLIPSE = 7


class DrawingSquiggleTechniques(IntEnum):
    """ INT Enum containing the different types of image.Draw foreground techniques"""
    SQUIGGLES = 1
    BIGSQUIGGLES = 2
    SMALLSQUIGGLES = 3
    DIRECTIONALSQUIGS = 4


class PILImageFilters(IntEnum):
    """ Image filters supported by PIL """
    BLUR = 1
    CONTOUR = 2
    DETAIL = 3
    EDGE_ENHANCE = 4
    EDGE_ENHANCE_MORE = 5
    EMBOSS = 6
    FIND_EDGES = 7
    SHARPEN = 8
    SMOOTH = 9
    SMOOTH_MORE = 10


def create_blank_canvas():
    """creates new image blank canvas"""
    image = Image.new("RGB", CANVAS_SIZE, BACKGROUND_COLOR)
    return image


def create_random_color():
    """returns random RGB color"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)


def denormalize(colormap):
    """Pillow accepts integers of 0 -> 255 for the color"""
    return [
        tuple(int(channel * 255) for channel in color)
        for color in colormap
    ]


def create_random_color_incolormap(colormap):
    """return random color within a specified colormap from matplotlib.cm"""
    palette = denormalize(colormap)
    return palette[random.randint(0, len(palette)-1)]


def create_random_point():
    """returns 2 random points within the bounds of the drawing canvas"""
    return (
        random.randint(0+DRAW_PADDING, MAX_PX_CANVAS-DRAW_PADDING),
        random.randint(0+DRAW_PADDING, MAX_PX_CANVAS-DRAW_PADDING)
    )


def create_random_angle():
    """returns random image from 0 to 360 degrees"""
    return random.randint(0, 360)


def draw_random_shapes(image, color):
    """Creates a random drawing - no preference - all techniques have equal probability"""
    random_technique = random.randint(1, len(DrawingShapeTechniques))
    draw_shapes_by_type(image, color, random_technique)


def draw_shapes_by_type(image, color, drawing_shape_type):
    """Creates a drawing of type DrawingShapeTechniques """
    draw = ImageDraw.Draw(image)

    initial_random_point = create_random_point()
    second_random_point = add_points_together(
        initial_random_point, (random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE),
                               random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE)))
    third_random_point = add_points_together(
        initial_random_point, (random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE),
                               random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE)))

    match drawing_shape_type:
        case DrawingShapeTechniques.LINE:
            draw.line((initial_random_point, second_random_point), fill=color)
        case DrawingShapeTechniques.CHORD:
            draw.chord((initial_random_point, second_random_point),
                       create_random_angle(), create_random_angle(),
                       fill=color, outline=(0, 0, 0), width=1)
        case DrawingShapeTechniques.PIESLICE:
            draw.pieslice((initial_random_point, second_random_point),
                          create_random_angle(), create_random_angle(),
                          fill=color, outline=(0, 0, 0), width=1)
        case DrawingShapeTechniques.ELLIPSE:
            draw.ellipse(
                (initial_random_point, second_random_point), fill=color, outline=(0, 0, 0), width=1)
        case DrawingShapeTechniques.RECTANGLE:
            draw.rectangle(
                (initial_random_point, second_random_point), fill=color, outline=(0, 0, 0), width=1)
        case DrawingShapeTechniques.POLYGON:
            draw.polygon((initial_random_point, second_random_point,
                         third_random_point), fill=color, outline=(0, 0, 0), width=1)
        case DrawingShapeTechniques.CONNECTEDLINES:
            draw_random_connected_lines(draw, color)


def draw_random_squiggles(image, color):
    """Creates a random foreground - the main worker function of this artmaker module"""
    draw = ImageDraw.Draw(image)
    random_technique = random.randint(1, len(DrawingSquiggleTechniques))

    match random_technique:
        case DrawingSquiggleTechniques.SQUIGGLES:
            draw_random_regularsquiggles(draw, color)
        case DrawingSquiggleTechniques.BIGSQUIGGLES:
            draw_random_bigsquiggle(draw, color)
        case DrawingSquiggleTechniques.SMALLSQUIGGLES:
            draw_random_smallsquiggles(draw, color)
        case DrawingSquiggleTechniques.DIRECTIONALSQUIGS:
            draw_random_directionsquig(draw, color)


def draw_random_smallsquiggles(draw, color):
    """Uses points to create some squiggles - takes in draw,color"""
    point = create_random_point()
    for _ in range(random.randint(0, 1500)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-1, 1), random.randint(-1, 1)))


def draw_random_regularsquiggles(draw, color):
    """Uses points to create some squiggles - takes in draw,color"""
    point = create_random_point()
    for _ in range(random.randint(0, 2500)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-3, 3), random.randint(-3, 3)))


def draw_random_bigsquiggle(draw, color):
    """Uses points to create some big squiggles - takes in draw,color as"""
    point = create_random_point()
    for _ in range(random.randint(0, 2500)):
        draw.point(point, fill=color)
        point = add_points_together(
            point, (random.randint(-15, 15), random.randint(-10, 10)))


def draw_random_directionsquig(draw, color):
    """Uses points to create some big squiggles - takes in draw,color as"""
    point = create_random_point()  # starting point
    angle = create_random_angle()

    for _ in range(random.randint(0, 5000)):
        angle += random.randint(-1, 1)  # random angle
        for _ in range(random.randint(0, 5)):
            draw.point(point, fill=color)
            point = add_points_together(
                point, (random.randint(0, 3) * math.cos(angle),
                        random.randint(0, 3) * math.sin(angle)))


def apply_random_filter(image):
    """ applies a random PIL Image Filter to the image"""
    random_filter = random.randint(1, len(PILImageFilters))
    # print(PILImageFilters(random_filter).name)
    match random_filter:
        case PILImageFilters.BLUR:
            return image.filter(ImageFilter.BLUR)
        case PILImageFilters.CONTOUR:
            return image.filter(ImageFilter.CONTOUR)
        case PILImageFilters.DETAIL:
            return image.filter(ImageFilter.DETAIL)
        case PILImageFilters.EDGE_ENHANCE:
            return image.filter(ImageFilter.EDGE_ENHANCE)
        case PILImageFilters.EDGE_ENHANCE_MORE:
            return image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        case PILImageFilters.EMBOSS:
            return image.filter(ImageFilter.EMBOSS)
        case PILImageFilters.FIND_EDGES:
            return image.filter(ImageFilter.FIND_EDGES)
        case PILImageFilters.SHARPEN:
            return image.filter(ImageFilter.SHARPEN)
        case PILImageFilters.SMOOTH:
            return image.filter(ImageFilter.SMOOTH)
        case PILImageFilters.SMOOTH_MORE:
            return image.filter(ImageFilter.SMOOTH_MORE)


def add_points_together(point1, point2):
    """adding tuples is done this way - thanks Google!"""
    zipped = zip(point1, point2)
    mapped = map(sum, zipped)
    return tuple(mapped)


def draw_random_connected_lines(draw, color):
    """draw random connected lines"""
    point = create_random_point()
    endpoint = point
    for _ in range(random.randint(0, 10)):
        endpoint = add_points_together(
            endpoint, (random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE),
                       random.randint(-MAX_SIZE_SHAPE, MAX_SIZE_SHAPE)))
        draw.line((point, endpoint), fill=color)
        point = endpoint


def draw_using_round_techniques(image, color):
    """ draw using only round techniques
    more suitable for drawings of organic things"""

    draw_random_squiggles(image, color)
    random_technique = random.randint(5, 7)
    draw_shapes_by_type(image, color, random_technique)


def draw_using_hardedge_techniques(image, color):
    """draw using hard edged techniques - good for
    non-organic things"""
    random_technique = random.randint(1, 4)
    draw_shapes_by_type(image, color, random_technique)


def returnrandomcolormap():
    """returns a random colormap"""
    random_map = random.randint(1, 10)

    match random_map:
        case 1:
            return matplotlib.cm.get_cmap("twilight").colors
        case 2:
            return matplotlib.cm.get_cmap("viridis").colors
        case 3:
            cmap = matplotlib.cm.get_cmap("summer")
            return cmap(np.arange(0, cmap.N))
        case 4:
            cmap = matplotlib.cm.get_cmap("spring")
            return cmap(np.arange(0, cmap.N))
        case 5:
            cmap = matplotlib.cm.get_cmap("autumn")
            return cmap(np.arange(0, cmap.N))
        case 6:
            cmap = matplotlib.cm.get_cmap("winter")
            return cmap(np.arange(0, cmap.N))
        case 7:
            cmap = matplotlib.cm.get_cmap("ocean")
            return cmap(np.arange(0, cmap.N))
        case 8:
            cmap = matplotlib.cm.get_cmap("terrain")
            return cmap(np.arange(0, cmap.N))
        case 9:
            cmap = matplotlib.cm.get_cmap("nipy_spectral")
            return cmap(np.arange(0, cmap.N))
        case 10:
            cmap = matplotlib.cm.get_cmap("rainbow")
            return cmap(np.arange(0, cmap.N))


def generate_image(maxoperations):
    """this is the main image generation method """
    image = create_blank_canvas()

    somethingwasdrawn = False
    random_technique = random.randint(1, 3)

    colormap = returnrandomcolormap()

    match random_technique:
        case 1:
            while not somethingwasdrawn:
                if bool(random.getrandbits(1)):
                    for _ in range(random.randint(0, maxoperations)):
                        draw_random_squiggles(
                            image, create_random_color_incolormap(colormap))
                    somethingwasdrawn = True

                if bool(random.getrandbits(1)):
                    for _ in range(random.randint(0, maxoperations)):
                        draw_random_shapes(
                            image, create_random_color_incolormap(colormap))
                    somethingwasdrawn = True

                if not somethingwasdrawn:
                    for _ in range(random.randint(0, maxoperations*5)):
                        draw_random_squiggles(
                            image, create_random_color_incolormap(colormap))
                    somethingwasdrawn = True
        case 2:
            for _ in range(random.randint(0, maxoperations)):
                draw_using_round_techniques(
                    image, create_random_color_incolormap(colormap))
        case 3:
            for _ in range(random.randint(0, maxoperations)):
                draw_using_hardedge_techniques(
                    image, create_random_color_incolormap(colormap))

    return image
