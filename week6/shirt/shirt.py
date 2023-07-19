import sys
from PIL  import Image, ImageOps
import os


def main():
    merge_images()


def check_argv():
    extentions = [ ".jpg", ".jpeg", ".png"]
    e_1 = os.path.splitext(sys.argv[1])
    e_2 = os.path.splitext(sys.argv[2])

    # Check the ammount of elements in the argv.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if e_1[1] != e_2[1]:
        sys.exit("Input and output have different extensions")
    if not e_1[1] in extentions:
        sys.exit("Invalid Input")
    if not e_2[1] in extentions:
        sys.exit("Invalid output")

def merge_images():
    check_argv()
    try:
        u_image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    user_image = ImageOps.fit(u_image, size)
    user_image.paste(shirt, shirt)
    user_image.save(sys.argv[2])

if __name__ == "__main__":
    main()