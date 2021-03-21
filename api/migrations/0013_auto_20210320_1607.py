# Generated by Django 3.1.7 on 2021-03-20 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_playlist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]