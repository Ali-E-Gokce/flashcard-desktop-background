from random import sample
"""
I scraped the colors off:
https://www.rapidtables.com/web/color/html-color-codes.html
The code reads the colors from a .txt file, then picks two randomly.
You can  use an array to increase speed if that is an issue
it takes around 5% of the time, but looking at the screen with the array
hurts my eyes, plust it consumes marginally more memory.
"""

def get_color():
    with open("colors.txt", "r") as f:
        colors = f.readlines()
    color1, color2 = sample(colors, 2)
    return color1, color2
