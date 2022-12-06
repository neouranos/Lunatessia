from django.urls import path
from lunatessia_chatterbot.views import ChatterBotAppView, ChatterBotApiView

urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
