from django.urls import path
from . import views

urlpatterns = [
    path('bar', views.bar, name='bar'),
]
