from django.db import models

import users.models


class Habits(models.Model):
    place = models.CharField(max_length=50, verbose_name='место')
    time = models.TimeField
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField
    linked = models.ForeignKey('self')
    period = models.IntegerField
    reward = models.CharField
    length = models.IntegerField
    is_public = models.BooleanField
    owner = models.ForeignKey(users.models.User)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
