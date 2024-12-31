#!/usr/bin/python

from PIL.Image import Image as IMAGE
from PIL import Image
from hashlib import sha256
from random import seed, getrandbits
from math import ceil
from sys import argv, stderr

class Properties:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Properties, cls).__new__(cls)
            cls.instance.init()
        return cls.instance
    def init(self):
        self.icon_width: int = 5
        self.icon_height: int = 5
        self.output_path: str = ""
        self.input_text: str = ""
        self.mirror = True

def error(msg: str, code: int = 1):
    print(msg, file=stderr)
    exit(code)

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

def generate_icon(text: str) -> IMAGE:
    properties = Properties()
    width: int = properties.icon_width
    height: int = properties.icon_height

    code: str = get_hashed(text)
    seed(int(code, 16)+width+height*65536)

    color: tuple[int, int, int, int] = get_color()

    image: IMAGE = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    for_width = width
    if properties.mirror:
        for_width = ceil(width/2)
    for x in range(for_width):
        for y in range(height):
            if getrandbits(1):
                image.putpixel((x, y), color)
                if properties.mirror:
                    image.putpixel((width-1-x, y), color)

    return image

def save_icon(icon: IMAGE) -> None:
    properties = Properties()
    width: int = properties.icon_width*32
    height: int = properties.icon_height*32

    icon = icon.resize((width, height), Image.NEAREST)

    output_path: str = get_output_path()
    icon.save(output_path, "png")

def get_output_path() -> None:
    properties = Properties()
    path: str = properties.output_path
    if path != "": return path

    path = properties.input_text+".png"
    return path

def process_args(arguments: list[str]) -> None:
    arguments.pop(0) # pop main file name
    process_help(arguments)
    process_output_path(arguments)
    process_width(arguments)
    process_height(arguments)
    process_no_mirror(arguments)
    process_input_text(arguments)

def process_help(arguments: list[str]) -> None:
    if len(arguments) == 0:
        print("""\
Usage: genicon [options] <text>

Options:
    -o <path>       Specify the output file name.
                    ('.png' will be added to the end if it does not include)
                        default: <input_text>.png
    -w <width>      Set width of the icon.
                        default: 5
    -h <height>     Set height of the icon.
                        default: 5
""", end="")
        exit(0)

def process_output_path(arguments: list[str]) -> None:
    if "-o" not in arguments: return
    
    index: int = arguments.index("-o")
    if len(arguments) <= index+1:
        error("Give an output path after '-o'")
    
    arguments.pop(index) # pop "-o"
    
    path: str = arguments.pop(index) # pop value
    if not path.endswith(".png"):
        path += ".png"
    Properties().output_path = path

def process_width(arguments: list[str]) -> None:
    if "-w" not in arguments: return
    
    index: int = arguments.index("-w")
    if len(arguments) <= index+1:
        error("Give a width value after '-w'")
    
    arguments.pop(index) # pop "-w"
    width: str = arguments.pop(index) # pop value
    if not width.isnumeric() and int(width) <= 0:
        error("Give a positive integer as a width value after '-w'")
    
    Properties().icon_width = int(width)

def process_height(arguments: list[str]) -> None:
    if "-h" not in arguments: return
    
    index: int = arguments.index("-h")
    if len(arguments) <= index+1:
        error("Give a height value after '-h'")
    
    arguments.pop(index) # pop "-h"
    height: str = arguments.pop(index) # pop value
    if not height.isnumeric() and int(height) <= 0:
        error("Give a positive integer as a height value after '-h'")
    
    Properties().icon_height = int(height)

def process_no_mirror(arguments: list[str]) -> None:
    for flag in ["-m", "--no-mirror"]:
        if flag in arguments:
            arguments.remove(flag)
            Properties().mirror = False

def process_input_text(arguments: list[str]) -> None:
    text: str = " ".join(arguments)
    Properties().input_text = text

def main() -> None:
    process_args(argv)
    text: str = Properties().input_text
    icon: IMAGE = generate_icon(text)
    save_icon(icon)

if __name__ == "__main__":
    main()
