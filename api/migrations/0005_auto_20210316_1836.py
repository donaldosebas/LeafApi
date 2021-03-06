# Generated by Django 3.1.7 on 2021-03-17 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='link',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='api.genre'),
        ),
    ]
