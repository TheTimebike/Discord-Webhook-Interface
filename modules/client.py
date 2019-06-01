import discord, aiohttp, asyncio
from .webhookhandler import WebhookHandler

class Client:
    def __init__(self):
        self._webhook_handler = WebhookHandler()
        self._loop = asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self._loop)
    
    def send_event(self, coro):
        setattr(self, "_send_event", coro)

    def run_event(self, event):
        self._loop.run_until_complete(self._run_event(event))

    async def _run_event(self, event):
        function = getattr(self, event)
        await function()

    async def send(self, url, message, author):
        await self._webhook_handler._send(url, message, author, self)

    async def delete(self, url):
        await self._webhook_handler._delete(url, self)