from django.shortcuts import render


def python(request):
    return render(request, 'python/python.html', {})


def python_slides(request):
    return render(request, 'python/python_slides.html', {})
