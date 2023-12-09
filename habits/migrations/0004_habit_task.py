# Generated by Django 4.2.7 on 2023-12-09 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('habits', '0003_alter_habit_options_remove_habit_linked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask', verbose_name='Ссылка на периодическую задачу'),
        ),
    ]