# Generated by Django 2.2.5 on 2019-09-13 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='videofilee',
            new_name='videofile',
        ),
    ]
