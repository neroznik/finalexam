from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class MyUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name='user', verbose_name='Пользователь')
    friends = models.ManyToManyField(get_user_model(), related_name='friends', blank=True, null=True, verbose_name='Друзья')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), related_name="sender", on_delete=models.CASCADE, verbose_name='Отправитель')
    reciever = models.ForeignKey(get_user_model(), related_name="reciever", on_delete=models.CASCADE, verbose_name='Получатель')
    text = models.TextField (max_length=5000, blank=True, null=False, verbose_name='Текст сообщения')
    created_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)

    def __str__(self):
        return f'{self.sender} to {self.reciever}'


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
