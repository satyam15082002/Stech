# Generated by Django 3.0.5 on 2020-07-09 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='grp',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
