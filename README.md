# GENICON

Generate simple icons based on text inputs.

<img src="./sample-icons/a.png" alt="a" width="80" height="80"> <img src="./sample-icons/42.png" alt="42" width="80" height="80"> <img src="./sample-icons/genicon.png" alt="genicon" width="80" height="80"> <img src="./sample-icons/icons created by genicon.png" alt="icons created by genicon" width="80" height="80"> <img src="./sample-icons/I love coding.png" alt="I love coding" width="80" height="80">

## Why need this?

- You can create random icons as the profile photo of the users based on their usernames. (Inspired by github.)
- You can visualize the id of anything in your program, game, etc. It is up to your imagination.

## How to use?

### Use as a command line tool

Clone the repo, and use command as described below.

```
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
```

---

### Import as a python script in your program

If you want to use this script as a part of your program, you can import `generation.py` script.

```python
import generation as genicon
```

---

You can generate icons as PIL image with this function:

```python
image = genicon.generate_image("a")
```

**Note:** The image will not be scaled. You can scale it up using `image.resize(...)`.

---

If you do not want to use a PIL image, you can retrieve the icon data regardless of the image type using the following function and create an image in your preferred format yourself.

```python
icon_data = genicon.generate_icon_data("a")
```

This will return a 2D list of tuples, where each tuple represents RGBA color with four integers in range(0, 256).
