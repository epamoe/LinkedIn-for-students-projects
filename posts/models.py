from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from users.models import Etudiant, Investisseur
import os
from PIL import Image
from django.utils import timezone

# creation de la classe Projet

class Comment(models.Model):
    
    title = models.CharField(max_length=600, blank=False)
    
    def __str__(self):
        return self.title
    

class Projet(models.Model):
    INVESTI = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]
    CATHEGORIES = [
        ('INFORMATIQUE','INFORMATIQUE'),
        ('AGRICULTURE','AGRICULTURE'),
        ('ELEVAGE','ELEVAGE'),
        ('SANTE','SANTE'),
        ('AUTRES','AUTRES')
    ]

    title = models.CharField('Titre du Projet', max_length=200)
    categorie = models.CharField('categorie projet', max_length=200, choices=CATHEGORIES, default='categorie')
    media = models.FileField(upload_to='documents/post_doc/', blank=True)
    image = models.ImageField(upload_to='image/post_image/', default='post.jpg', blank=True)
    investi = models.CharField(choices=INVESTI, default='Non', max_length=10, blank=True)

    description = models.TextField(max_length=500)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projet')
    date_post = models.DateTimeField('date_post',default=timezone.now, blank=True)


    def __str__(self):
        return  f'{self.etudiant.user.last_name} Post- {self.title}'


# model pour le Chat

class Room(models.Model):
    name = models.CharField(max_length=100)
    # inv = models.CharField(max_length=100)
    # etu = models.CharField(max_length=1000)
    inv = models.ForeignKey(Investisseur, on_delete=models.CASCADE, related_name="room")
    etu = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='room')
    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    # room = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')

