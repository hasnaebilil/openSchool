from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('events/', include('events.urls')),
    path('algorithmic/', include('algorithmic.urls')),
    path('python/', include('python.urls')),
]
