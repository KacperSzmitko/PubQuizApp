# Generated by Django 2.2.6 on 2019-12-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_gamepreferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepreferences',
            name='entry_fee',
            field=models.FloatField(default=5),
        ),
        migrations.AddField(
            model_name='gamepreferences',
            name='extra_question_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepreferences',
            name='game_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamepreferences',
            name='nd_place_reward',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='gamepreferences',
            name='rd_place_reward',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='gamepreferences',
            name='st_place_reward',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamepreferences',
            name='current_round',
            field=models.IntegerField(default=1),
        ),
    ]
