#-*- coding: utf-8 -*-
from stock.models import Matos
from django.contrib import admin

class MatosAdmin(admin.ModelAdmin):

	list_display = ('nom', 'categorie', 'sous_categorie')
	list_filter = ('categorie', 'sous_categorie')
	fieldsets = [
        ('Général',  {
            'fields': ['nom', 'categorie', 'sous_categorie', 'image']}),
        ('Informations supplémentaires', {
        	'fields': ['q_stock', 'details', 'marque', 'model'], 
        	'classes': ['collapse']}),
        ('Projecteur', {
            'fields': ['type_proj', 'puissance_proj', 'tension_proj', 'angle_min', 'angle_max', 'has_dmx'],
            'classes': ['collapse']}),
        ('Microphone', {
        	'fields': ['directivite', 'sensibilite', 'type_micro'],
        	'classes' : ['collapse']}),
    ]

admin.site.register(Matos, MatosAdmin)



