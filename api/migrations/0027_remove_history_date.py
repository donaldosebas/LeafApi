# Generated by Django 3.1.7 on 2021-05-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20210501_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='date',
        ),
    ]
