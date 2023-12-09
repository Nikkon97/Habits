from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator, FrequencyValidator, IsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычек"""
    validators = [
        DurationValidator(field='duration'),
        FrequencyValidator(field='frequency'),
        IsPleasantValidator(field1='is_pleasant', field2='linked_habit', field3='reward')
    ]

    class Meta:
        model = Habit
        fields = ['pk', 'place', 'time', 'action', 'is_pleasant', 'linked_habit', 'reward', 'frequency', 'duration',
                  'is_public']
