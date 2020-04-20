import aiohttp

class TelegramBot:

    def __init__(self, auth_token, session, offset = 0):
        self.url = f"""https://api.telegram.org/bot{auth_token}/"""
        self.session = session
        self.offset = offset

    async def process_session(self):
        update_url = self.url + "getUpdates"
        params = {'offset': self.offset}
        async with self.session.get(update_url, params = params) as resp:
            update = await resp.json()
            if update['ok']:
                for resp_result in update['result']:
                    chat_id = await self.get_chat_id(resp_result)
                    message = await self.send_message(chat_id, 'hello')
                    self.offset = (await self.get_update_id(resp_result) + 1)

    async def get_chat_id(self, request):
        return request['message']['chat']['id']

    async def get_update_id(self, request):
        return request['update_id']

    async def get_message(self, request):
        return request['message']

    async def send_message(self, chat_id, text):
        send_url = self.url + "sendMessage"
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        async with self.session.get(send_url, params=params) as resp:
            # wait for future response for get request while it reads body
            html = await resp.json()
            return html