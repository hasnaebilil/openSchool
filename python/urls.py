from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.python, name='python'),
    path('python_slides/', views.python_slides, name='python-slides'),
]
