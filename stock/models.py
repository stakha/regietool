#-*- coding: utf-8 -*-
from django.db import models
from django import forms

class Matos(models.Model):

	CATEGORIE_CHOICES = (
		('lum', 'Lumière'),
		('son', 'Son'),
		('vid', 'Vidéo'),
		('pla', 'Plateau'),
		)

	SOUS_CATEGORIE_CHOICES = [
		("Lumière",(
			('prj', "Projecteur"),
			('pup', "Jeux d'orgue"),
			('dim', "Gradateur"),
			)),
		("Son", (
			('enc', 'Enceinte'),
			('mic', 'Microphone'),
			('amp', 'Amplificateur'),
			('mix', 'Table de mixage'),
			('prc', 'Processing'),
			)),
		("Vidéo", (
			('vip', 'Vidéo projecteur'),
			)),
		('cab', 'Câble'),
		('sup', 'Support'),
		]

	TYPE_PROJ_CHOICES = [
		('Traditionnel',(
			('pc', 'Plan convexe'),
			('fre', 'Fresnel'),
			('dec', 'Découpe'),
			('par', 'PAR'),
			('qua', 'Quartz'),
			('bat', 'Basse tension'),
			)),
		('Asservi', (
			('lyr', 'Lyre'),
			('pal', 'Par led'),
			('str', 'Stromboscope'),
			)),	
		('aut', 'Autre'),
		]

	TYPE_MICRO_CHOICES = (
		('DYN', 'Micro dynamique'),
		('CON', 'Micro à condensateur'),
		('RUB', 'Micro à ruban'),
		)

	DIRECTIVITE_CHOICES = (
		('OMN', 'Omnidirectionnel'),
		('CAR', 'Cardioïde'),
		('HYP', 'HyperCardioïde'),
		('CAN', 'Canon'),
		)
	
	nom = models.CharField('nom usuel', max_length = 50)
	image = models.ImageField(upload_to = 'img/', blank=True)
	categorie = models.CharField('catégorie',max_length=3, choices=CATEGORIE_CHOICES)
	sous_categorie = models.CharField('sous catégorie',max_length=3, choices=SOUS_CATEGORIE_CHOICES)
	q_stock = models.IntegerField('quantité', max_length=5, default=1)
	details = models.TextField('caractéristiques', blank=True)
	marque = models.CharField('marque', max_length=32, blank=True)
	model = models.CharField('modèle', max_length=32, blank=True)
	poids = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, help_text = 'En kilogramme(s)', default = 0)
	hauteur = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text = 'En mètre(s)', default = 0)
	largeur = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text = 'En mètre(s)', default = 0)
	profondeur = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text = 'En mètre(s)', default = 0)
	date_achat = models.DateField("date d'achat", blank=True, null=True)
	date_check = models.DateField("vérifié le ", blank=True, null=True)
	date_modif = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')
	date_ajout = models.DateTimeField(auto_now_add = True, verbose_name = "Date d'ajout")
	asbl = models.NullBooleanField('Matériel ASBL', blank=True, null=True) 

# Projecteur
	type_proj = models.CharField('type de projecteur', max_length=3, blank=True, null=True, choices=TYPE_PROJ_CHOICES)
	puissance_proj = models.IntegerField('puissance', max_length=5, blank=True, null=True, help_text='En watt(s)')
	tension_proj = models.IntegerField('tension', max_length=3, blank=True, null=True, help_text='En volt(s)')
	angle_min = models.IntegerField('angle minimum', max_length=3, blank=True, null=True, help_text='En degré(s)')
	angle_max = models.IntegerField('angle maximum', max_length=3, blank=True, null=True ,help_text='En degré(s)')
	has_dmx = models.NullBooleanField('DMX', null=True, blank=True)

# Micro
	directivite = models.CharField('directivité', max_length=3, choices= DIRECTIVITE_CHOICES, blank=True)
	sensibilite = models.DecimalField('sensibilité', max_digits=4, decimal_places=2, blank=True, null=True, help_text = 'En mV/Pa')
	type_micro = models.CharField('type de micro', max_length=21, choices= TYPE_MICRO_CHOICES, blank=True)
	freq_min = models.IntegerField(max_length=5, blank=True, null=True, help_text='En hertz')
	freq_max = models.IntegerField(max_length=5, blank=True, null=True, help_text='En hertz')
	
# Enceinte

		
# Ampli

	

	def __unicode__(self):
		return u"%s" %self.nom 

class SearchForm(forms.Form):
	CATEGORIE_CHOICES = (
		('None', '---------'),
		('lum', 'Lumière'),
		('son', 'Son'),
		('vid', 'Vidéo'),
		('pla', 'Plateau'),
		)
	SOUS_CATEGORIE_CHOICES = [
	('None', '---------'),
	("Lumière",(
		('prj', "Projecteur"),
		('pup', "Jeux d'orgue"),
		('dim', "Gradateur"),
		)),
	("Son", (
		('enc', 'Enceinte'),
		('mic', 'Microphone'),
		('amp', 'Amplificateur'),
		('mix', 'Table de mixage'),
		('prc', 'Processing'),
		)),
	("Vidéo", (
		('vip', 'Vidéo projecteur'),
		)),
	('cab', 'Câble'),
	('sup', 'Support'),
	]

	categorie = forms.ChoiceField(choices=CATEGORIE_CHOICES, label="catégorie")
	sous_categorie = forms.ChoiceField(choices=SOUS_CATEGORIE_CHOICES, label="sous catégorie")




