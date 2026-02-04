from django.shortcuts import render,redirect
from money.models import Income,Expenditure
from .forms import IncomeForm,ExpenditureForm

# Create your views here.
def money_home_view(request):
    incomes = Income.objects.filter(user = request.user).order_by('-date')
    expenditures = Expenditure.objects.filter(user = request.user).order_by('-date')

    records = []

    for inc in incomes:
        records.append({
            'type': '収入',
            'date': inc.date,
            'amount': inc.amount,
        })

    for exp in expenditures:
        records.append({
            'type': '支出',
            'date': exp.date,
            'amount': exp.amount,
        })

    # 日付順に並べ替え
    records.sort(key=lambda x: x['date'], reverse=True)

    return render(request, 'money_home.html', {'records': records})

def income_view(request):
    if request.method == "POST":
        form = IncomeForm(request.POST, request.FILES)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('money:money_home')
    else:
        form = IncomeForm()
    return render(request, "income.html",{'form':form})

def expenditure_view(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST, request.FILES)
        if form.is_valid():
            expenditure = form.save(commit=False)
            expenditure.user = request.user
            expenditure.save()
            return redirect('money:money_home')
    else:
        form = ExpenditureForm()
    return render(request, "expenditure.html",{'form':form})