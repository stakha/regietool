# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to=b'/stock/photo_matos/')),
                ('categorie', models.CharField(default=b'unknown', max_length=11, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'Lumi\xc3\xa8re', ((b'trad', b'Traditionnel'), (b'led', b'Led'), (b'lyre', b'Lyre'), (b'dimmer', b'Dimmer'), (b'cable', b'C\xc3\xa2ble'), (b'support', b'Support'), (b'console', b'Console'), (b'consommable', b'Consommable'), (b'autre', b'Autre'))), (b'Son', ((b'enceinte', b'Enceinte'), (b'micro', b'Microphone'), (b'ampli', b'Amplification'), (b'processing', b'Processing'), (b'mixer', b'Mixer'), (b'cable', b'C\xc3\xa2ble'), (b'support', b'Support'), b'autre')), (b'Video', ((b'vp', b'Vid\xc3\xa9o Projecteur'), (b'support', b'Support'), (b'cable', b'C\xc3\xa2ble'), (b'autre', b'Autre'))), (b'Machinerie', ((b'levage', b'Levage'), (b'tissu', b'Tissu'), (b'support', b'Support'), (b'autre', b'Autre'))), (b'unknown', b'Unknown')])),
                ('q_stock', models.IntegerField(default=1, max_length=5, verbose_name=b'quantit\xc3\xa9')),
                ('details', models.TextField(verbose_name=b'd\xc3\xa9tails', blank=True)),
                ('marque', models.CharField(max_length=32, verbose_name=b'marque', blank=True)),
                ('model', models.CharField(max_length=32, verbose_name=b'mod\xc3\xa8le', blank=True)),
                ('poids', models.DecimalField(decimal_places=1, default=0, max_digits=5, blank=True, help_text=b'En kilogrammes', null=True)),
                ('hauteur', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, help_text=b'En m\xc3\xa8tres', null=True)),
                ('largeur', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, help_text=b'En m\xc3\xa8tres', null=True)),
                ('profondeur', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, help_text=b'En m\xc3\xa8tres', null=True)),
                ('date_achat', models.DateField(null=True, verbose_name=b"date d'achat", blank=True)),
                ('date_check', models.DateField(null=True, verbose_name=b'v\xc3\xa9rifi\xc3\xa9 le ', blank=True)),
                ('date_modif', models.DateField(auto_now=True, verbose_name=b'Date de modification')),
                ('date_ajout', models.DateField(auto_now_add=True, verbose_name=b"Date d'ajout")),
                ('link', models.URLField(verbose_name=b'Site du fabricant', blank=True)),
                ('asbl', models.NullBooleanField(verbose_name=b'Mat\xc3\xa9riel ASBL')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
