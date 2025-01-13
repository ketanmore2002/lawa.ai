import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Accept the WebSocket connection

    async def disconnect(self, close_code):
        pass  # Handle disconnection

    async def receive(self, text_data):
        # Handle incoming message
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Echo the message back to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
