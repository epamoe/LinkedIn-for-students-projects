# Generated by Django 4.0.4 on 2022-05-25 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('posts', '0003_projet_image1_projet_image2_projet_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projet', to='users.etudiant'),
        ),
    ]