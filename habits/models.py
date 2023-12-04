from django.db import models

import users.models


class Habit(models.Model):
    place = models.CharField(max_length=50, verbose_name='место')
    time = models.TimeField
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField
    linked = models.ForeignKey('self', on_delete=models.CASCADE)
    period = models.IntegerField
    reward = models.CharField
    length = models.IntegerField
    is_public = models.BooleanField
    owner = models.ForeignKey(users.models.User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
