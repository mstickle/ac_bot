import json
import urllib.parse

import asyncio
import aiohttp

async def main():
    # Open config file and get auth token
    with open('config.json') as f:
        config = json.load(f)

    # Create auth token url
    auth_token = f"""https://api.telegram.org/bot{config['auth_token']}/"""

    # Set up string and make it url compatible
    hello_str = "hello world"
    text = urllib.parse.quote(hello_str)

    # hard coded until something retrieves it
    chat_id = -1001155429271

    # Create url with message to send
    url = auth_token+"sendMessage?chat_id={0}&text={1}".format(chat_id, text)

    # Start client session
    async with aiohttp.ClientSession() as session:
        # Send message by making a get request
        async with session.get(url) as resp:
            # async with session.get(url) reads header
            # wait for future response for get request while it reads body
            html = await resp.json()
            print(html)


if __name__ == '__main__':
    # start event loop
    # loop = asyncio.get_event_loop()
    # # add future to event loop and runs until complete
    # loop.run_until_complete(main())

    # starts event loop and runs until future is complete then destroys event loop
    asyncio.run(main())
