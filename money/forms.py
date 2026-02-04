from django import forms
from .models import Income,Expenditure

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            'amount',
            'type',
            'date',
        ]
        label = {
            'amount': '金額',
            'type': '種類',
            'date': '日付'
        }
        widgets = {
            'amount': forms.TextInput(attrs={'placeholder':'＊必須'}),
            'date' : forms.DateInput(attrs={'type':'date'}),
        }

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = [
            'title',
            'amount',
            'date',
            'category',
            'memo',
        ]
        label = {
            'title':'内容',
            'amount': '金額',
            'date': '日付',
            'category': 'カテゴリー',
            'memo': 'メモ'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'＊必須'}),
            'amount': forms.TextInput(attrs={'placeholder':'＊必須'}),
            'date' : forms.DateInput(attrs={'type':'date'}),
            'memo': forms.Textarea(attrs={'rows': 3}),
        }