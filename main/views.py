from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ChatGPTForms, ContactForm
from .service.openai_service import OpenAIService
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
chatId = '1338444137'

bot = telebot.TeleBot(token)


def home(request):
    chat_form = ChatGPTForms()
    contact_form = ContactForm()
    return render(request, 'main/home.html', {'chat_form': chat_form, 'contact_form': contact_form})


def ask_gpt(request):
    if request.method == "POST":
        form = ChatGPTForms(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']

            openai_service = OpenAIService()
            model = "gpt-3.5-turbo"
            messages = [{"role": "user", "content": f'{question}, отвечай пожалуйста на русcком языке'}]
            response = openai_service.get_chat_answer(model, messages)
            # response = 'it is temporary txt'

            return render(request, 'main/home.html', {'response': response, 'form': form})
    return render(request, 'main/home.html', {'form': ChatGPTForms()})


def send_contact(request):
    print('it works!!!')
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            telegram_contact = form.cleaned_data['telegram_contact']
            print(telegram_contact)
            # Здесь будет логика для отправки контакта
            bot.send_message(chatId, telegram_contact)
            success_message = "Ваш контакт был отправлен"
            return redirect('home')
    return redirect('home')


def contact(request):
    return render(request, 'main/contact.html')
