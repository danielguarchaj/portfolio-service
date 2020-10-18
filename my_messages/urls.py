  
from django.urls import path, include

from . import views

app_name = 'my_messages'

urlpatterns = [
    path('', views.MessageCreate.as_view(), name='messages')
]