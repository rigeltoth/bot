from rest_framework import viewsets

from .models import Bot
from .serializer import BotSerializer

class BotViewSet(viewsets.ModelViewSet):
  queryset = Bot.objects.all()
  serializer_class = BotSerializer

