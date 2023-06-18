from django.urls import path
from . import views

urlpatterns = [
    path('bar', views.bar, name='bar'),
    path('scatter_data', views.scatter_data, name='scatter_data'),
    path('scatter', views.scatter, name='scatter'),
]
