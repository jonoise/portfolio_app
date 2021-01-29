from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'frontend/index.html')


def portfolio(request):
    return render(request, 'frontend/portfolio.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def next(request):
    return render(request, 'frontend/next.html')
