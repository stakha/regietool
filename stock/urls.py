#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

	url(r'^$', 'stock.views.home'),
	url(r'^(?P<matos_id>\d+)/$', 'stock.views.detail_matos'),
	)



