# Main program to generate images - to be called from command prompt
# Uses artmaker module by Brian Lawrence
import artmaker

DIRECTORY = "images/"

if __name__ == "__main__":
    print("This program generates random images.. starting now!")
    for i in range(artmaker.NUMBER_OF_GENERATED_IMAGES):
        IMAGENAME = "genImage"+str(i+1)+".png"
        THEIMAGE = artmaker.generate_image(100)
        THEIMAGE.save(DIRECTORY+IMAGENAME)
        print(IMAGENAME + " generated.")
