# Generated by Django 4.0.4 on 2022-05-25 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='image3',
        ),
    ]
