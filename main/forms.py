from django import forms


class ChatGPTForms(forms.Form):
    question = forms.CharField(label="Ведите сюда ваш вопрос для ChatGPT. Что-то вроде: Какая площадь Америки?",
                               max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш вопрос...'}))


class ContactForm(forms.Form):
    telegram_contact = forms.CharField(label='Ваш контакт в Telegram',
                                       max_length=255,
                                       widget=forms.TextInput(attrs={'placeholder': 'Введите ваш контакт в Telegram.'}))
