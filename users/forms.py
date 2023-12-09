from django.contrib.auth import forms
from django.contrib.auth import get_user_model


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )


class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )
