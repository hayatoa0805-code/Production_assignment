from django.shortcuts import render, redirect, get_object_or_404
from oshis.models import Oshi
from .forms import OshiForm
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
@login_required
def oshi_home_view(request):
    oshis = Oshi.objects.all()
    return render(request, 'oshis/oshi_home.html', {'oshis': oshis})

@login_required
def oshi_add_view(request):
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

def oshi_detail_view(request, pk):
    oshi = get_object_or_404(Oshi, pk=pk, user=request.user)
    days_elapsed = 0
    if oshi.met_day:
        today = date.today()
        days_elapsed = (today - oshi.met_day).days

    if days_elapsed >= 3650:
        rank = "mythic"
    elif days_elapsed >= 1000:
        rank = "legend"
    elif days_elapsed >= 365:
        rank = "gold"
    elif days_elapsed >= 100:
        rank = "silver"
    else:
        rank = "bronze"

    return render(
        request,
        'oshis/oshi_detail.html',
        {
            'oshi': oshi,
            'days_elapsed':days_elapsed,
            'rank':rank,
        }
        )

@login_required
def oshi_edit_view(request,pk):
    oshi = get_object_or_404(Oshi,pk = pk, user=request.user)

    if request.method == 'POST':
        form = OshiForm(request.POST, request.FILES, instance=oshi)
        if form.is_valid():
            form.save()
            return redirect('oshis:oshi_detail',pk=pk)
    else:
        form = OshiForm(instance=oshi)
    return render(
        request, 
        'oshis/oshi_edit.html', 
        {
            'form': form,
            "oshi":oshi
        })

@login_required
def oshi_delete_view(request,pk):
    oshi = get_object_or_404(Oshi, pk=pk)

    if request.method == "POST":
        oshi.delete()
        return redirect("oshis:oshi_home")

    return render(
        request,
        "oshis/oshi_delete.html",
        {"oshi": oshi}
    )
