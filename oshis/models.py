from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class OshiCategory(models.TextChoices):
    ARTUST="artist","アーティスト"
    ACTIVIST = "activist","配信者"
    VOCALOID = "vocaloid","ボーカロイド"
    CHARACTER = "character","キャラクター"
    VTUBER = "vtuber","Vチューバー"
    IDOL= "idol","アイドル"
    PERFORMER = "performer","演者"
    OTHER = "other","その他"

class Oshi(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name=('oshis')
        )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#666666")
    group_name = models.CharField(max_length=20,null = True,blank = True)
    birthday = models.DateField(null=True, blank=True)
    aniversary = models.DateField(null=True,blank=True)
    met_day = models.DateField(
        null = True,
        blank=True,
        default=timezone.now
        )
    input_formats = ['%m-%d']

    category = models.CharField(
        max_length=20,
        choices = OshiCategory.choices,
        default='未設定'
    )
    image = models.ImageField(upload_to = 'oshi_icons/',null=True,blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name