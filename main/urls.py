from django.urls import path
from .views import KursView

urlpatterns = [
    path('', KursView, name='kurs'),
]
