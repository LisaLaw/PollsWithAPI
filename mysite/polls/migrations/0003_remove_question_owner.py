# Generated by Django 3.1.1 on 2020-09-21 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200918_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='owner',
        ),
    ]
