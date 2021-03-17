# Generated by Django 3.1.7 on 2021-03-16 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.genre'),
            preserve_default=False,
        ),
    ]