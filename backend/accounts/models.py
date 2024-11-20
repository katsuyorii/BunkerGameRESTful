from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    username = models.CharField(verbose_name='Никнейм', max_length=30)
    avatar = models.ImageField(verbose_name='Изображение профиля', upload_to='users_profile_avatars', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email