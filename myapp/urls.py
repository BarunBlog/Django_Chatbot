from django.urls import path
from simple_chatbot.views import SimpleChatbot

urlpatterns = [
    path("", SimpleChatbot.as_view())
]