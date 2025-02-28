import sys
import os.path
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        l = [".png", ".jpeg", ".jpg"]
        ex1 = os.path.splitext(sys.argv[1])
        ex2 = os.path.splitext(sys.argv[2])
        if ex1[-1] not in l:
            sys.exit("Invalid input")
        if ex2[-1] not in l:
            sys.exit("Invalid output")
        if ex1[-1] == ex2[-1]:
            shirt()
        else:
            sys.exit("Input and output have different extension")

def shirt():
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])
        size = shirt.size
        before = ImageOps.fit(before, size)
        before.paste(shirt, box = (0, 0), mask = shirt)
        before.save(sys.argv[2], format=None)
        print
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
