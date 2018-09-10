# Generated by Django 2.1 on 2018-08-30 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postto',
            field=models.CharField(default='All', max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[('none', 'Everyone'), ('friendsoffriends', 'Friends of Friends'), ('friends', 'Just Friends')], default='none', max_length=20),
        ),
    ]
