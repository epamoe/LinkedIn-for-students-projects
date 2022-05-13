from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os

# Create your models here.

 

# creation la classe Utilisateur

def renommer_image(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    listExt = ['png', 'jpg', 'tif', 'bmp', 'jpeg', 'gif']
    if instance.user.username:
        noms = instance.user.last_name.split(' ')
        idUser = instance.user.id
        n = ""
        nom_image = ""
        for nom in noms:
            n += ("_"+nom)
        nom_image = (str(idUser)+n)
        filename = "photos_profile/{}.{}".format(nom_image, "png")
        return os.path.join(upload_to, filename)

class Utilisateur(models.Model):

    ville = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=100, null=True)
    photoProfil = models.ImageField(upload_to='image/profile_pics/', default='default.jpeg', blank=True)
    question = models.CharField(max_length=100)
    reponse = models.CharField(max_length=100)

    # pour que la classe ne crée pas une table dans la BD
    class Meta:
        abstract = True
    


# creation de la Classe Etudiant

def renommer_fichier(instance, filename):
    upload_to = 'documents/'
    if instance.user.username:
        noms = instance.user.last_name.split(' ')
        idUser = instance.user.id
        n = ""
        nom_fichier = ""
        for nom in noms:
            n += ("_"+nom)
        nom_fichier = (str(idUser)+n)
        filename = "fiches_inscription/{}.{}".format(nom_fichier, "png")
        return os.path.join(upload_to, filename)

class Etudiant(Utilisateur):
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant')

    NIVEAUX = [
        ('BAC + 1', 'BAC + 1'),
        ('BAC + 2', 'BAC + 2'),
        ('BAC + 3', 'BAC + 3'),
        ('BAC + 4',  'BAC + 4'),
        ('BAC + 5', 'BAC + 5'),
        ('Doctorant', 'Doctorant'),
    ]
    niveauEtude = models.CharField(choices=NIVEAUX, default='BAC + 1', max_length=100)
    universite = models.CharField(max_length=100)
    fiche_inscription = models.FileField(upload_to=renommer_fichier, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'



# creation de la classe Investisseur

class Investisseur(Utilisateur):
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investisseur')

    profession = models.CharField(max_length=100)
    objectifs = models.CharField(max_length=300)
    entreprise = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    image = models.ImageField(default='default.jpeg', upload_to='photo_profil')

    def __str__(self):
        return f'{self.user.username} Profile'