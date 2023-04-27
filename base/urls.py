from .views import BaseView
from django.urls import path

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]
