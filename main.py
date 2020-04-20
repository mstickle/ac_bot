import json
import urllib.parse

import asyncio
import aiohttp

from telegram_bot import TelegramBot

async def main():
    # Open config file and get auth token
    with open('config.json') as f:
        config = json.load(f)

    async with aiohttp.ClientSession() as session:
        test_bot = TelegramBot(config['auth_token'], session)
        try:
            while True:
                await test_bot.process_session()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    # starts event loop and runs until future is complete then destroys event loop
    asyncio.run(main())
