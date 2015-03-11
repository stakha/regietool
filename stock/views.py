#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404 , render_to_response
from django.template import RequestContext
from stock.models import *
import pdb

def home(request):

	list_matos = Matos.objects.all().order_by('date_modif').reverse()
	form = SearchForm()
	if request.method == 'POST':
		form = SearchForm(request.POST)
		choix_categorie = request.POST['categorie']
		choix_sous_categorie = request.POST['sous_categorie']
		if choix_categorie != 'None':
			if choix_sous_categorie != 'None':
				list_matos = Matos.objects.filter(categorie=choix_categorie).filter(sous_categorie=choix_sous_categorie).order_by('date_modif')
				pass
			else : 
				list_matos = Matos.objects.filter(categorie=choix_categorie)
				pass
		elif choix_sous_categorie != 'None':
			list_matos = Matos.objects.filter(sous_categorie=choix_sous_categorie)
			pass

		else : 
			list_matos = Matos.objects.all().order_by('categorie', 'sous_categorie')
			pass
		return render_to_response('stock/home.html', 
		{'list_matos': list_matos, 'form': form}, 
		context_instance=RequestContext(request))
	else:
		return render_to_response('stock/home.html', 
		{'list_matos': list_matos, 'form': form}, 
		context_instance=RequestContext(request))

def detail_matos(request, matos_id):
    matos = get_object_or_404(Matos, pk=int(matos_id))
    
    if matos.sous_categorie == 'prj':
    	return render_to_response('stock/matos_projecteur.html', {'matos': matos }, context_instance=RequestContext(request))
    elif matos.categorie == 'enc':
    	return render_to_response('stock/matos_enceinte.html', {'matos': matos }, context_instance=RequestContext(request))
    elif matos.categorie == 'mic':
    	return render_to_response('stock/matos_micro.html', {'matos': matos }, context_instance=RequestContext(request))
    elif matos.categorie == 'pla':
    	return render_to_response('stock/matos_plateau.html', {'matos': matos }, context_instance=RequestContext(request))
    else:
    	return render_to_response('stock/detail_matos.html', {'matos': matos }, context_instance=RequestContext(request))
