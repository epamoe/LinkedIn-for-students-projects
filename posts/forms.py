from dataclasses import field
from pyexpat import model
from django import forms
from .models import Projet


class ProjetForm(forms.ModelForm):
	class Meta():
		model = Projet
		fields = [
			'title',
			'categorie',
			'media',
			'image',
			'investi',
			'description',
			'etudiant',
            
		]
