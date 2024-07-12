import json

import g4f
from channels.generic.websocket import AsyncWebsocketConsumer
from g4f.client import Client

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        question = data['question']
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": question}]

        async for message in self.get_chat_answer(model, messages):
            await self.send(text_data=json.dumps({
                'message': message
            }))

    async def get_chat_answer(self, model: str, messages: list):
        response = g4f.ChatCompletion.create(
            model=model,
            messages=messages,
            stream=True,
        )
        for i message in response:
            print(message, flush=True, end='')
            return message
