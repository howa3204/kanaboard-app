from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'landing/home.html', context)

def about(request):
    context = {}
    return render(request, 'landing/about.html', context)

def privacy(request):
    context = {}
    return render(request, 'landing/privacy.html', context)

def terms(request):
    context = {}
    return render(request, 'landing/terms.html', context)

def refund(request):
    context = {}
    return render(request, 'landing/refund.html', context)
