from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def settings_view(request):
    return render(request, 'settings.html')

def test_view(request):
    return render(request, 'test.html')