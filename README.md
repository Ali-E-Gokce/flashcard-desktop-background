Takes a csv file with words and their meanings, and changes your desktop
background to a flashcard like screen to help you memorize those words, which
updates periodically. I use it for GRE  and foreign language vocab,
but it can be used for any other purpose as well. You can run the code again
to refresh the background page without wait.

Background.jpeg is a sample backgroun.

You can make csv file containing words that are difficult to remember,
and you will see them everytime you look at your desktop.

The color of the text and the background are random, because I feel that
this makes me more likely to pay attention to the screen. If you want a more
aesthetic background, I have found beige (f5f5dc) text
salmon (#FA8072) background to be pleasing.


If you have more than one desktop, most of your desktops should change,
although sometimes some don't and I don't know why. The desktop
where you called the script from might behave oddly. This is not an issue for
me since I use several desktops anyway. Using another desktop to open a
screen (e.g. finder) open on the odd-desktop fixes the issue.

It needs to be running in the background constantly to work, but since
it uses the sleep method, it is not using any significant resources when
not changing the background.
THIS WORKS ON MACOS MOJAVE VERSION 10.14.15
I DON'T GUARANTEE IT WILL WORK ON ANY OTHER MACOS VERSION!!!
Changing the desktop background from the command line is system specific,
and might not work on other systems. If you want to run it on another
operating system, all you need to change is
To run it on windows, you can look use ctypes.

The computer might momentarily freeze when the background is being changed,
this is unlikely to be noticeable unless the BACKGROUND_SWAP_INTERVAL is very low.

For information on how to customize the program for your need,
take a look at comments.txt
