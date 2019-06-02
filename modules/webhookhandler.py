import discord, aiohttp, asyncio

class WebhookHandler:
    def __init__(self):
        self._last_url = None
        self._last_webhook = None

    async def _start(self, url, handler):
        async with aiohttp.ClientSession() as session:
            if self._last_url == url:
                return self._last_webhook
            else:
                _webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(handler._session))
                self._last_webhook = _webhook
                self._last_url = url
                return self._last_webhook
    
    async def _send(self, url, message, author, handler):
        _webhook = await self._start(url, handler)
        await _webhook.send(message, username=author)

    async def _delete(self, url, handler):
        _webhook = await self._start(url, handler)
        await _webhook.delete()