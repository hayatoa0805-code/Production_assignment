from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
class GoodsCategory(models.TextChoices):
    ACRYLIC_KEYHOLDER = 'acrylic_keyholder', "アクキー"
    ACRYLIC_STAND = 'acrylic_stand', "アクスタ"
    BADGE = 'badge', "缶バッジ"
    FIGURE = 'figure', "フィギュア"
    DISC = 'disc', "CD・DVD・BD"
    BOOK = 'book', "書籍"
    OTHER = "other","その他"

class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goods'
        )
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='goods',
        null=False,
        blank=False,
    )
    goods_name = models.CharField(max_length=20)
    category = models.CharField(
        max_length=20,
        choices=GoodsCategory.choices,
        default=GoodsCategory.OTHER
        )
    price = models.DecimalField(max_digits=10, decimal_places=0)
    num = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
        )
    total_price = models.DecimalField(
        editable=False,
        default=0,
        max_digits=10,
        decimal_places=0,
        )
    goods_image = models.ImageField(upload_to='goods_images/', null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.num
        super().save(*args, **kwargs)

    def __str__(self):
        return self.goods_name