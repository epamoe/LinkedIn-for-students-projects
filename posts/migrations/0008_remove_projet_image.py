# Generated by Django 4.0.4 on 2022-05-26 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_projet_image_alter_projet_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='image',
        ),
    ]