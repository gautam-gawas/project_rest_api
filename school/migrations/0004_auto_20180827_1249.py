# Generated by Django 2.1 on 2018-08-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20180826_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
