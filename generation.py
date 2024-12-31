from PIL.Image import Image as IMAGE
from PIL import Image
from hashlib import sha256
from random import seed, getrandbits
from math import ceil

def get_hashed(text: str) -> str:
    return sha256(text.encode()).hexdigest()

def get_color() -> tuple[int, int, int, int]:
    while True:
        red  : bool = getrandbits(1) == 1
        green: bool = getrandbits(1) == 1
        blue : bool = getrandbits(1) == 1
        if not (red == green == blue == 0):
            break

    return (
        192 if red   else 64,
        192 if green else 64,
        192 if blue  else 64,
        255
    )

def generate_icon_data(text: str, width: int = 5, height: int= 5, mirror: bool = True) -> list[list[tuple[int, int, int, int]]]:
    code: str = get_hashed(text)
    seed(int(code, 16)+width+height*65536)

    color: tuple[int, int, int, int] = get_color()

    icon_data: list[list[tuple[int, int, int, int]]] = [[(0, 0, 0, 0) for _ in range(height)] for _ in range(width)]

    for_width = width
    if mirror:
        for_width = ceil(width/2)
    for x in range(for_width):
        for y in range(height):
            if getrandbits(1):
                icon_data[x][y] =  color
                if mirror:
                    icon_data[width-1-x][y] = color

    return icon_data

def generate_image(text: str, width: int, height: int, mirror: bool = True) -> IMAGE:
    icon_data = generate_icon_data(text, width, height, mirror)

    image: IMAGE = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), icon_data[x][y])
    
    return image
