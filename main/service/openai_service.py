import datetime

from g4f.client import Client
import datetime
question = 'Какая площадь Минска'
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": f'{question}, отвечай пожалуйста на русcком языке'}]


def time_checker(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(datetime.datetime.now()-start_time)
        return result
    return wrapper


@time_checker
class OpenAIService:
    @staticmethod
    def get_chat_answer(self, model: str, messages: list) -> str:
        client = Client()
        response = client.chat.completions.create(model=model, messages=messages)
        if 'sorry' in response.choices[0].message.content:
            return 'Повторите попытку сервер перегружен'
        print(response.choices[0].message.content)
        return response.choices[0].message.content


# res = OpenAIService.get_chat_answer(model, messages)





