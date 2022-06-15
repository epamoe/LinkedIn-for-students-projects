# Generated by Django 4.0.4 on 2022-06-14 22:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(max_length=600)),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
                ('time_com', models.TimeField(auto_now_add=datetime.datetime(2022, 6, 14, 22, 37, 34, 150988, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(max_length=600)),
                ('date_reponse', models.DateTimeField(auto_now_add=True)),
                ('time_rep', models.TimeField(auto_now_add=datetime.datetime(2022, 6, 14, 22, 37, 34, 151612, tzinfo=utc))),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('user_reponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Titre du Projet')),
                ('categorie', models.CharField(max_length=200, verbose_name='categorie projet')),
                ('media', models.FileField(blank=True, upload_to='documents/post_doc/')),
                ('image', models.ImageField(blank=True, default='default.jpeg', upload_to='images/post_image/')),
                ('investi', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=10)),
                ('description', models.TextField(max_length=500, null=True)),
                ('date_post', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date de publication')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projet', to='users.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.projet'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
