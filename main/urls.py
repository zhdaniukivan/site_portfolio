from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('ask_gpt/', views.ask_gpt, name='ask_gpt'),
    path('send_contact/', views.send_contact, name='send_contact'),
]
