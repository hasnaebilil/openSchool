from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses'),
    path('new/', views.new),
    path('search_courses/', views.search_courses, name='search-courses'),
]
