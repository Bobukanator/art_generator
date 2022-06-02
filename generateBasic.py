# Main program to generate images - to be called from command prompt
# Uses artmaker module by Brian Lawrence
import artmaker

DIRECTORY = "images/"
NUMBER_OF_IMAGES_TO_CREATE = 2


def create_images_and_save():
    """creates 100 random images - how suave"""
    print(F"Randomly creating and saving {NUMBER_OF_IMAGES_TO_CREATE} images")
    for i in range(NUMBER_OF_IMAGES_TO_CREATE):
        image_name = "genImage"+str(i+1)+".png"
        the_image = artmaker.generate_image(250)
        the_image.save(DIRECTORY+image_name)
        print(DIRECTORY+image_name)


if __name__ == "__main__":
    print("This program generates random images.. starting now!")
    create_images_and_save()
