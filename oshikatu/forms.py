from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="ユーザー名",
        error_messages={
            "required": "ユーザー名を入力してください",
            "unique": "このユーザー名は既に使われています",
        },
    )

    email = forms.EmailField(
        label="メールアドレス",
        error_messages={
            "required": "メールアドレスを入力してください",
            "invalid": "正しいメールアドレスを入力してください",
        },
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    error_messages = {
        "password_mismatch": "パスワードが一致しません",
    }