from django.contrib import admin
from .models import Projet, Room, Message, Commentaire, Reponse


# Register your models here.

class AdminProjet(admin.ModelAdmin):
	list_display   = ('title', 'etudiant', 'date_post', 'categorie')
	list_filter    = ('title','categorie',)
	search_fields  = ('title', 'etudiant')
admin.site.register(Projet, AdminProjet)

admin.site.register(Room)
admin.site.register(Message)

class AdminCom(admin.ModelAdmin):
	list_display   = ('auteur', 'projet', 'date_added')

admin.site.register(Commentaire, AdminCom)
admin.site.register(Reponse)