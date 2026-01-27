from django import forms
from .models import Goods

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = [
            'event',
            'goods_name',
            'category',
            'price',
            'num',
            'goods_image',
            'memo',
        ]
        labels = {
            'event': 'イベント',
            'goods_name': 'グッズ名',
            'category': 'カテゴリー',
            'price': '価格',
            'num': '個数',
            'goods_image': '画像',
            'memo': 'メモ',
        }
        widgets = {
            'price': forms.NumberInput(attrs={'min': 0}),
            'memo': forms.Textarea(attrs={'rows': 3}),
        }

class GoodsIdForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = [
            'goods_name',
            'category',
            'price',
            'num',
            'goods_image',
            'memo',
        ]
        labels = {
            'goods_name': 'グッズ名',
            'category': 'カテゴリー',
            'price': '価格',
            'num': '個数',
            'goods_image': '画像',
            'memo': 'メモ',
        }
        widgets = {
            'memo': forms.Textarea(attrs={'rows': 3}),
        }