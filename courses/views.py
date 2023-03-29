from django.http import HttpResponse
from django.shortcuts import render
from .models import Course


def search_courses(request):
    if request.method == "POST":
        searched = request.POST['searched']
        courses = Course.objects.filter(name__contains=searched)
        return render(request, 'courses/search_courses.html', {'searched': searched, 'courses': courses})
    else:
        return render(request, 'courses/search_courses.html', {'searched': searched})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def new(request):
    return HttpResponse('New Course')
