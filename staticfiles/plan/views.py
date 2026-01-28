from django.shortcuts import render

# Create your views here.

def plan_home_view(request):
    return render(request,"plan/plan_home.html")