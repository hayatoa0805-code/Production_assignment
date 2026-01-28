from django.db import models
from django.conf import settings

# Create your models here.
class TypeChoices(models.TextChoices):
    SALARY = 'salary','給料'
    BONUS = 'bonus','ボーナス'
    GIFT = 'gift','ギフト'
    OTHER = 'other','その他'

class Income(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=20,
        choices=TypeChoices.choices
    )
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.amount}円"

class GoodsCategory(models.TextChoices):
    GOODS = 'goods',"グッズ",
    SUPERCHAT = 'superchat','スパチャ'
    OTHER = "other","その他"

class Expenditure(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateField()
    memo = models.TextField(blank = True)
    category = models.CharField(
        max_length=20,
        choices = GoodsCategory.choices
    )

    def __str__(self):
        return f"{self.title} - {self.amount}円"