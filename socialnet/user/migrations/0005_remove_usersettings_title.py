# Generated by Django 2.0.7 on 2018-11-15 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181115_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='title',
        ),
    ]
