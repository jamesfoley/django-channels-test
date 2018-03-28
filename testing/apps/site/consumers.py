from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SiteConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['id']
        self.group_name = f'group_{self.group_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'command',
                'message': content
            }
        )

    async def command(self, event):
        await self.send_json(content=event['message'])
