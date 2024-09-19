from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    has_book = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"   

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.age >= 18:
            self.account_type = 0
        elif 13 <= self.age < 18:
            self.account_type = 1
        else:
            self.account_type = 2

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]