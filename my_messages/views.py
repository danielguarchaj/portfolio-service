from rest_framework.generics import CreateAPIView

from .serializers import MessageSerializer
from .models import Message


class MessageCreate(CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()