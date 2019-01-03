from dotenv import load_dotenv
load_dotenv()

import os

from client import PixelFlutBot

# Get the config and start the bot...
def main():
    server = {
        'host': os.environ['HOST'],
        'port': int(os.environ['PORT']),
        'password': os.environ['OAUTH_TOKEN'],
    }
    pixelflut = {
        'host': os.environ['PIXELFLUT_HOST'],
        'port': int(os.environ['PIXELFLUT_PORT'])
    }
    channel = os.environ['CHANNEL_NAME']
    nickname = os.environ['BOT_USERNAME']

    bot = PixelFlutBot(channel, nickname, server, pixelflut)
    bot.start()

if __name__ == "__main__":
    main()
