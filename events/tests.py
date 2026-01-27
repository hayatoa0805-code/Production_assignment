from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event
from goods.models import Goods

class GoodsDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )

        self.event = Event.objects.create(
            event_id=1,
            title="テストイベント",
            user=self.user
        )

        self.goods1 = Goods.objects.create(
            goods_name="グッズ1",
            price=1000,
            quantity=2,
            total_price=2000,
            user=self.user,
            event=self.event
        )

        self.goods2 = Goods.objects.create(
            goods_name="グッズ2",
            price=500,
            quantity=1,
            total_price=500,
            user=self.user,
            event=self.event
        )


        self.event.goods.add(self.goods1, self.goods2)

        self.client.login(
            username="testuser",
            password="password"
        )