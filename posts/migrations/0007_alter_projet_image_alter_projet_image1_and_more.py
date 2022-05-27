# Generated by Django 4.0.4 on 2022-05-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_projet_image_alter_projet_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='image',
            field=models.ImageField(blank=True, upload_to='image//'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='image1',
            field=models.ImageField(blank=True, upload_to='image/post/'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='image2',
            field=models.ImageField(blank=True, upload_to='image/post_image/'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='image3',
            field=models.ImageField(blank=True, upload_to='image/post-image/'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='media',
            field=models.FileField(blank=True, upload_to='image/doc/post/'),
        ),
    ]
