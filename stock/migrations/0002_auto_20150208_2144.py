# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matos',
            name='sous_categorie',
            field=models.CharField(default=b'unknown', max_length=11, verbose_name=b'sous cat\xc3\xa9gorie', choices=[(b'Lumi\xc3\xa8re', ((b'trad', b'Traditionnel'), (b'led', b'Led'), (b'lyre', b'Lyre'), (b'dimmer', b'Dimmer'), (b'cable', b'C\xc3\xa2ble'), (b'support', b'Support'), (b'orgue', b"Jeux d'orgue"), (b'consommable', b'Consommable'), (b'autre', b'Autre'))), (b'Son', ((b'enceinte', b'Enceinte'), (b'micro', b'Microphone'), (b'ampli', b'Amplification'), (b'processing', b'Processing'), (b'mixer', b'Mixer'), (b'cable', b'C\xc3\xa2ble'), (b'support', b'Support'), (b'autre', b'Autre'))), (b'Video', ((b'vp', b'Vid\xc3\xa9o Projecteur'), (b'support', b'Support'), (b'cable', b'C\xc3\xa2ble'), (b'autre', b'Autre'))), (b'Machinerie', ((b'levage', b'Levage'), (b'tissu', b'Tissu'), (b'support', b'Support'), (b'autre', b'Autre'))), (b'unknown', b'Ind\xc3\xa9termin\xc3\xa9')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='categorie',
            field=models.CharField(default=b'unknown', max_length=12, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'lumi\xc3\xa8re', b'Lumi\xc3\xa8re'), (b'son', b'Son'), (b'video', b'Vid\xc3\xa9o'), (b'machinerie', b'Machinerie'), (b'unknown', b'Ind\xc3\xa9termin\xc3\xa9'), (b'none', b'Veuillez choisir une cat\xc3\xa9gorie')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='details',
            field=models.TextField(verbose_name=b'caract\xc3\xa9ristiques', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='image',
            field=models.ImageField(upload_to=b'photos/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='nom',
            field=models.CharField(max_length=32, verbose_name=b'nom usuel'),
            preserve_default=True,
        ),
    ]
