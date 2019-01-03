# Woah.... Yeah... This is ghetto.
# This abuses the banner figlet font to draw text...
from pyfiglet import Figlet

def render(text):
    f = Figlet(font='banner')
    return f.renderText(text).split('\n')
