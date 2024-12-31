#!/usr/bin/python

from PIL.Image import Image as IMAGE
from PIL import Image
from sys import argv, stderr
from generation import generate_image

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
    -o <path>           Specify the output file name.
                        ('.png' will be added to the end if it is not included)
                            default: <input_text>.png
    -w <width>          Set width of the icon.
                            default: 5
    -h <height>         Set height of the icon.
                            default: 5
    -m, --no-mirror     Generate icon without mirroring.
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
    properties = Properties()
    icon: IMAGE = generate_image(
        properties.input_text,
        properties.icon_width,
        properties.icon_height,
        properties.mirror,
    )
    save_icon(icon)

if __name__ == "__main__":
    main()
