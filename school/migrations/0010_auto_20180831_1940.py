# Generated by Django 2.1 on 2018-08-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20180831_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]