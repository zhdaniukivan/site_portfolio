import os


class SmsSender():
    def __init__(self, user_phone, message_text):
        self.user_phone = user_phone
        self.message_text = message_text

    @staticmethod
    def send_sms(user_phone, message_text):
        print(f"Я отправляю смс с текстом: {message_text} на номер {user_phone}")



res = SmsSender.send_sms('+375292819815', 'help')






