from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    oshi_id = models.ForeignKey(
        'oshis.Oshi',
        on_delete=models.CASCADE,
        related_name='events',
        null=True,
        blank=True
    )
    date = models.DateField()
    location = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    event_image = models.ImageField(
        upload_to='event_images/',
        null=True,
        blank=True,
        )
    goods_image = models.ImageField(
        upload_to = 'goods_list_images/',
        null = True,
        blank = True,
    )
    memo = models.TextField(null=True,blank=True)
    
    def total_price(self):
        return sum(goods.total_price for goods in self.goods.all())
    
    def __str__(self):
        return self.title