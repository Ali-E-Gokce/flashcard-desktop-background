from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from get_color import get_color
import pandas as pd
import subprocess
from time import sleep

#where the generated picture will be saved
OUT_PATH = "/Users/alierengokcelioglu/desktop/try_stuff/background.jpeg"
#how much empty distance to leave on the right side of the screen
#depends on how full your desktop is.
#You might want to keep it low if you have very long input sentences
RIGHT_GAP = 800
#name of the file where the vocabulary is saved
INPUT_FILE = "vocab.csv"
#you can find other fonds online
WORD_FONT = ImageFont.truetype('Roboto-LightItalic.ttf', 48)
TEXT_FONT = ImageFont.truetype('Roboto-Light.ttf', 48)
#the background is changed every 4 hours
BACKGROUND_SWAP_INTERVAL = 4*60*60
#this is the script that changes the desktop background
#you should replace this with a script that works on your machine
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "{}"
end tell
END
killall Dock"""

#this won't work if there is more than one monitor attached
#but is the only way I could think of that does not require
#extra dependencies and works regardless of OS
def get_screen_size():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    heigth = root.winfo_screenheight()
    return width, heigth

#gets a random word and meaning from your list
def get_vocab(INPUT_FILE):
    df = pd.read_csv(INPUT_FILE)
    vocab_pair = df.sample(n = 1)
    word = vocab_pair["Word"].to_string(index = False)
    meaning = vocab_pair["Meaning"].to_string(index = False)
    return word, meaning



#split the sentence as necessary to fit on screen
#doesn't check for height, unlikely that it would be an issue
#returns list of lines/sentences
def split_sentence(text):
    lines = []
    screen_width, screen_height = get_screen_size()
    #the width of the sentence in the given font
    text_width = TEXT_FONT.getsize(text)[0]

    if text_width < screen_width:
        lines = [text]
    else:
        words = text.split(" ")
        sentence = ""
        #adds words to the sentence until the line exceeds screen width,
        #then moves on to a new line
        for i in words:
            if TEXT_FONT.getsize(sentence)[0] + RIGHT_GAP < screen_width:
                sentence += i + " "
            else:
                lines.append(sentence)
                sentence = ""
        #append last sentence, unless it's an empty sentnece
        if sentence != "":
            lines.append(sentence)
    return lines


#makes the background picture
def draw():
    width, height = get_screen_size()
    word, meaning = get_vocab(INPUT_FILE)
    lines = split_sentence(meaning)
    text_height = TEXT_FONT.getsize(meaning)[1]
    text_color, background_color =  get_color()
    im = Image.new("RGB", (width, height), background_color)
    d = ImageDraw.Draw(im)
    black = (0, 0, 0)
    y_offset = 50
    x_offset = 10
    d.text((x_offset, y_offset), word, fill = text_color, font = WORD_FONT)
    y_offset += 100
    for line in lines:
        y_offset += text_height
        d.text((x_offset, y_offset), line, fill = text_color, font = TEXT_FONT)
    im.save('{}'.format(OUT_PATH), optimize = True)




def new_desktop_background():
    draw()
    subprocess.Popen(SCRIPT.format(OUT_PATH), shell=True)
    #subprocess.Popen("killall Dock", shell=True)


if __name__ == "__main__":
    while True:
        new_desktop_background()
        sleep(BACKGROUND_SWAP_INTERVAL)
