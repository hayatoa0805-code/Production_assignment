from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from money.models import Income,Expenditure
from .forms import IncomeForm,ExpenditureForm

# Create your views here.
# ホーム
@login_required
def money_home_view(request):
    incomes = Income.objects.filter(user = request.user).order_by('-date')
    expenditures = Expenditure.objects.filter(user = request.user).order_by('-date')

    records = []

    for inc in incomes:
        records.append({
            'model': 'income',
            'pk': inc.pk,
            'type': '収入',
            'date': inc.date,
            'amount': inc.amount,
        })

    for exp in expenditures:
        records.append({
            'model': 'expenditure',
            'pk': exp.pk,
            'type': '支出',
            'date': exp.date,
            'amount': exp.amount,
        })

    records.sort(key=lambda x: x['date'], reverse=True)

    return render(
        request,
        'money/money_home.html',
        {
            'records': records
        })

# 収入
@login_required
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
    return render(
        request,
        "money/income.html",
        {
            'form':form
        })

@login_required
def income_edit_view(request,pk):
    income = get_object_or_404(Income,pk = pk, user = request.user)

    if request.method == "POST":
        form = IncomeForm(request.POST, instance = income)
        if form.is_valid():
            form.save()
            return redirect('money:money_home')
    else:
        form = IncomeForm(instance = income)
    
    return render(
        request,
        'money/income_edit.html',
        {
            'form':form,
            'income':income,
        })

@login_required
def income_delete_view(request,pk):
    income = get_object_or_404(Income, pk = pk, user = request.user)

    if request.method == 'POST':
        income.delete()
        return redirect('money:money_home')

    return render(
        request,
        'money/income_delete.html',
        {
            'income':income,
        }
    )


# 支出
@login_required
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
    return render(
        request,
        "money/expenditure.html",
        {
            'form':form
        })

@login_required
def expenditure_edit_view(request,pk):
    expenditure = get_object_or_404(Expenditure,pk = pk,user = request.user)

    if request.method == "POST":
        form = ExpenditureForm(request.POST, instance = expenditure)
        if form.is_valid():
            form.save()
            return redirect('money:money_home')
    else:
        form = ExpenditureForm(instance = expenditure)

    return render(
        request,
        'money/expenditure_edit.html',
        {
            'expenditure':expenditure,
            'form':form,
        }
    )


@login_required
def expenditure_delete_view(request, pk):
    expenditure = get_object_or_404(Expenditure, pk = pk, user = request.user)

    if request.method == 'POST':
        expenditure.delete()
        return redirect('money:money_home')
    
    return render(
        request,
        'money/expenditure_delete.html',
        {
            'expenditure':expenditure,
        }
    )