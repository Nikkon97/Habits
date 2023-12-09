from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

from users.models import User, NULLABLE


class Habit(models.Model):
    place = models.CharField(max_length=50, verbose_name='место выполнения')
    time = models.TimeField(default=timezone.now, verbose_name="время выполнения")
    action = models.CharField(max_length=100, null=False, blank=False, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name="флаг приятной привычки")
    linked_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name='периодичность выполнения в днях')
    reward = models.CharField(max_length=100, verbose_name="вознаграждение", **NULLABLE)
    duration = models.PositiveIntegerField(default=120, verbose_name='продолжительность выполнения')
    is_public = models.BooleanField(default=True, verbose_name='флаг публикации')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец", **NULLABLE)
    task = models.ForeignKey(PeriodicTask, on_delete=models.SET_NULL, verbose_name='Ссылка на периодическую задачу',
                             **NULLABLE)

    def __str__(self):
        loop_self = self
        message = f"я буду {self.action} в {self.time} в {self.place}\nВремя на выполнение: {self.duration} секунд\n"
        while True:
            if loop_self.reward:
                return message + f"Вознаграждение: {loop_self.reward}"
            elif loop_self.linked_habit is None:
                return message
            else:
                loop_self = loop_self.linked_habit

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = 'Привычки'
