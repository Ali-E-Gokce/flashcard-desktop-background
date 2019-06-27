THIS WORKS ON MACOS MOJAVE VERSION 10.14.15
I DON'T GUARANTEE IT WILL WORK ON ANY OTHER MACOS VERSION!!!
Changing the desktop background from the command line is system specific,
and might not work on other systems. If you want to run it on another
operating system, all you need to change is
To run it on windows, you can look use ctypes.

The computer might momentarily freeze when the background is being changed,
this is unlikely to be noticeable unless the BACKGROUND_SWAP_INTERVAL is very low.

The variables that you need to change to cusomtize the program are on
the top of the code. The variables are as follows:

OUT_PATH = "/Users/alierengokcelioglu/desktop/try_stuff/background.jpeg"

RIGHT_GAP:
  How much gap there should be between the text and the right side of the screen.

INPUT_FILE:
  The .csv file where the vocabulary is stored. The first column should be Word,
  where the words are stored, the second Meaning, where the meaning is stored.
  The names are case sensetive.

WORD_FONT = ImageFont.truetype('Roboto-LightItalic.ttf', 48)
  Font of the word
TEXT_FONT = ImageFont.truetype('Roboto-Light.ttf', 48)
  Font of the text. More fonts can be downloaded online.

BACKGROUND_SWAP_INTERVAL:
  how often the background should change, in seconds.

SCRIPT:
  The script that is run in the terminal to change the background.
  This will depend on your operating system, and you probably will have to
  change it.
