from g4f.client import Client


class OpenAIService:
    @staticmethod
    def get_chat_answer(self, model: str, messages: list) -> str:
        client = Client()
        response = client.chat.completions.create(model=model, messages=messages)
        if 'sorry' in response.choices[0].message.content:
            return 'Повторите попытку сервер перегружен'
        print(response.choices[0].message.content)
        return response.choices[0].message.content
