import json

from channels.generic.websocket import AsyncWebsocketConsumer


class MessagingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.messaging_channel = "message_channel"

        # Join room group
        await self.channel_layer.group_add(self.messaging_channel, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.messaging_channel, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["type"]
        if message=="message":
        # Send message to room group
            await self.channel_layer.group_send(
                self.messaging_channel, {"type": "send_message", "message": text_data_json["encrypted_message"],"sender": text_data_json["sender"]}
            )

        else:
             await self.channel_layer.group_send(
                self.messaging_channel, {"type": "send_keys", "message":  text_data_json["message"]}
            )

    # Receive message from room group
    async def send_keys(self, event):
        message = event["message"]
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"type":"key","message": message}))


    async def send_message(self, event):
        message = event["message"]
        sender = event["sender"]
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"type":"message","sender": sender,"message": message}))