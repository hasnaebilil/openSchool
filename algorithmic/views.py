from django.http import HttpResponse
from django.shortcuts import render


def algorithmic(request):
    return render(request, 'algorithmic/algorithmic.html', {})
