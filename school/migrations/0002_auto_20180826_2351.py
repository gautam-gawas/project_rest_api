# Generated by Django 2.1 on 2018-08-26 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='forms',
        ),
        migrations.AddField(
            model_name='project',
            name='forms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_req_2', to='school.Form'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_req_3', to=settings.AUTH_USER_MODEL),
        ),
    ]
