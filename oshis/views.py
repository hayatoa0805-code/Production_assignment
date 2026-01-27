from django.shortcuts import render, redirect
from oshis.models import Oshi
from .forms import OshiForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    oshis = Oshi.objects.all()
    return render(request, 'oshis/oshi_home.html', {'oshis': oshis})

@login_required
def add_view(request):
    if request.method == 'POST':
        form = OshiForm(request.POST, request.FILES)
        if form.is_valid():
            oshi = form.save(commit=False)
            oshi.user = request.user
            oshi.save()
            return redirect('oshis:oshi_home')
    else:
        form = OshiForm()
    return render(request, 'oshis/oshi_add.html', {'form': form})