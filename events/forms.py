from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'oshi_id',
            'date',
            'location',
            'event_image',
            'goods_image',
            'memo',
        ]
        labels = {
            'title': 'イベント名',
            'oshi_id': '推し',
            'date': '日付',
            'location': '場所',
            'event_image': 'イベント画像',
            'goods_image':'グッズ者写真',
            'memo': '説明',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'memo': forms.Textarea(attrs={'rows': 3}),
        }