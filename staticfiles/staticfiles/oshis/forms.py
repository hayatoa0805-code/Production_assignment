from django import forms
from .models import Oshi

class OshiForm(forms.ModelForm):
    class Meta:
        model = Oshi
        fields = [
            'name',
            'group_name',
            'birthday',
            'aniversary',
            'met_day',
            'category',
            'image',
            'notes',
        ]
        labels = {
            'name': '名前',
            'group_name': 'グループ名',
            'birthday': '誕生日',
            'aniversary': '記念日',
            'met_day': '出会った日',
            'category': 'カテゴリ',
            'image': '画像',
            'notes': 'メモ',
        }
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'aniversary': forms.DateInput(attrs={'type': 'date'}),
            'met_day': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        input_formats = ['%m月%d日']