from django.urls import path
from bot import views

urlpatterns = [
  path('', views.render_bots, name='bots')
]