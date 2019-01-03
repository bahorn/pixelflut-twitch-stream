import telnetlib
from PIL import Image

import text as prettyText

class PixelFlutDrawer:
    def __init__(self, host, port):
        self.s = telnetlib.Telnet(host, port)
        self.screen()

    # Fetch the screen width/height
    def screen(self):
        self.s.write(b'SIZE\n')
        _, width, height = self.s.read_until(b'\n').split()
        self.width = int(width)
        self.height = int(height)
        return (self.width, self.height)

    # Single Pixel drawing.
    def pixel(self, x, y, color, scale=1):
        for w in range(scale):
            for h in range(scale):
                msg = bytes('PX {} {} {}\n'.format(x+w, y+h, color).encode('ascii'))
                self.s.write(msg)

    # Text
    def text(self, x, y, color, text, scale=1):
        body = prettyText.render(text)
        for iy in range(0, len(body)):
            for ix in range(0, len(body[iy])):
                if body[iy][ix] == '#':
                    self.pixel(x+ix*scale, y+iy*scale, color, scale)

    # Draw an image from the library
    def image(self, x, y, image, scale=1):
        # go though each pixel and use the draw function
        try:
            im = Image.open(image)
        except:
            return
        width, height = im.size
        rgb_im = im.convert('RGB')
        for ix in range(0, width):
            for iy in range(0, height):
                r, g, b = rgb_im.getpixel((ix, iy))
                color = self.hex_code(r, g, b)
                self.pixel(x+ix*scale, y+iy*scale, color, scale)

    # Convert the RGB values into a hex code to send along.
    def hex_code(self, r, g, b):
        return '{:02x}{:02x}{:02x}'.format(r, g, b)

if __name__ == "__main__":
    pfd = PixelFlutDrawer('127.0.0.1', 1337)
    pfd.screen()
    pfd.pixel(100, 100, 'ff00ff', scale=100)
    pfd.image(200, 200, 'res/imgs/nyan.png', scale=1)
    pfd.text(500, 500, 'ff00ff', 'Woah dude! Hack The Planet!', scale=10)
