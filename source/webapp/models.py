from django.db import models
from django.contrib.auth import get_user_model


class MyUser(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name='user', verbose_name='Пользователь')
    friends = models.ManyToManyField(get_user_model(), related_name='friends', blank=True, null=True, verbose_name='Друзья')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

