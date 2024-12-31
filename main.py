#!/usr/bin/python

from PIL.Image import Image as IMAGE
from PIL import Image
from hashlib import sha256
from random import seed, getrandbits
from math import ceil

def get_input() -> str:
    print("enter some text: ", end="")
    while True:
        data: str = input()
        if data != "":
            return data

def get_hashed(text: str) -> str:
    return sha256(text.encode()).hexdigest()

def generate_icon(text: str) -> IMAGE:
    code: str = get_hashed(text)
    seed(int(code, 16))
    
    width = 5
    height = 5

    red  : bool = getrandbits(1) == 1
    green: bool = getrandbits(1) == 1
    blue : bool = getrandbits(1) == 1

    color: tuple[int, int, int, int] = (
        192 if red   else 64,
        192 if green else 64,
        192 if blue  else 64,
        255
    )

    image: IMAGE = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    for x in range(ceil(width/2)):
        for y in range(height):
            if getrandbits(1):
                image.putpixel((x, y), color)
                image.putpixel((width-1-x, y), color)

    return image

def save_icon(icon: IMAGE) -> None:
    icon = icon.resize((256, 256), Image.NEAREST)
    icon.save("icon.png")

def main() -> None:
    text: str = get_input()
    icon: IMAGE = generate_icon(text)
    save_icon(icon)

if __name__ == "__main__":
    main()
