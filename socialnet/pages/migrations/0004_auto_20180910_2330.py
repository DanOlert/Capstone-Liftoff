# Generated by Django 2.0.7 on 2018-09-11 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180910_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='musicembed',
            field=models.CharField(blank=True, default=None, max_length=1500, null=True),
        ),
    ]
