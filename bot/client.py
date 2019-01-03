#!/usr/bin/env python

# This code sucks.

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import shlex

from parse import *

import usage
import images

from draw import PixelFlutDrawer as PixelFlut

# So many better ways of doing this....
def validate_hexcode(value):
    if len(value) not in [6, 8]:
        return False
    for c in value:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            return False
    return True

class PixelFlutBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, pixelflut):
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(server['host'], server['port'], server['password'])],
            nickname,
            nickname
        )
        self.channel = channel
        self.pixelflut = PixelFlut(pixelflut['host'], pixelflut['port'])
        self.width, self.height = self.pixelflut.screen()

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(":", 1)
        channel = e.target
        if a[0][0] == '!':
            # send pixelflut command
            response = self.parse_command(a[0])
            if response != None:
                # send a message to the user letting them know of their error
                c.privmsg(channel, response)

    # Figure out what to do with the command.
    def parse_command(self, command):
        split = shlex.split(command)
        # Quick bit of validation to drop commands that we don't know of.
        if split[0] not in ['!px', '!image', '!text', '!help']:
            return 'Invalid Command!'
        if split[0] == '!px':
            # validate length of command
            if len(split) not in [4, 5]:
                return usage.px
            scale = 10
            color = ''
            try:
                x = int(split[1])
                y = int(split[2])
                if validate_hexcode(split[3]):
                    color = split[3]
                else:
                    return usage.px
            except:
                return usage.px
            if len(split) == 5:
                try:
                    scale = int(split[4])
                except:
                    pass
            self.pixelflut.pixel(x, y, color, scale)
        elif split[0] == '!image':
            # Parse the input..
            if len(split) not in [4, 5]:
                return usage.image
            scale = 1
            try:
                x = int(split[1])
                y = int(split[2])
                if split[3] in images.approved:
                    image = images.approved[split[3]]
            except:
                return usage.image
            if len(split) == 5:
                try:
                    scale = int(split[4])
                except:
                    pass
            # OK. Now trigger the command.
            self.pixelflut.image(x, y, image, scale)
        elif split[0] == '!text':
            if len(split) not in [5, 6]:
                return usage.text
            scale = 10
            color = ''
            try:
                x = int(split[1])
                y = int(split[2])
                if validate_hexcode(split[3]):
                    color = split[3]
                else:
                    return usage.text
                text = split[4]
            except:
                return usage.text
            if len(split) == 6:
                try:
                    scale = int(split[5])
                except:
                    pass
            self.pixelflut.text(x, y, color, text, scale)
        elif split[0] == '!help':
                return usage.info
