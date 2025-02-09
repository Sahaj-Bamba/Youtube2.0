# Generated by Django 2.2.5 on 2019-09-18 00:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0007_auto_20190918_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reports',
            field=models.ManyToManyField(related_name='commentreports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='reports',
            field=models.ManyToManyField(related_name='videoreports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='report',
        ),
        migrations.AddField(
            model_name='comment',
            name='report',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='video',
            name='report',
        ),
        migrations.AddField(
            model_name='video',
            name='report',
            field=models.IntegerField(default=0),
        ),
    ]
