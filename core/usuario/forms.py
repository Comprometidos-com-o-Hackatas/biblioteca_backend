from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    model = Usuario
    fields = ("email",) 