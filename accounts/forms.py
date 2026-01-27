from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # ← 独自 User を参照

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # ← ここを独自 User に
        fields = ('username', 'email', 'password1', 'password2')