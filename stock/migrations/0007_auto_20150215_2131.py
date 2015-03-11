# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20150210_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matos',
            name='categorie',
            field=models.CharField(max_length=3, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'LUM', b'Lumi\xc3\xa8re'), (b'SON', b'Son'), (b'VID', b'Vid\xc3\xa9o'), (b'PLA', b'Plateau')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Cat_Matos',
        ),
        migrations.AlterField(
            model_name='matos',
            name='image',
            field=models.ImageField(upload_to=b'img/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='sous_categorie',
            field=models.CharField(max_length=3, verbose_name=b'sous cat\xc3\xa9gorie', choices=[(b'PRO', b'Projecteur'), (b'ENC', b'Enceinte'), (b'MIC', b'Microphone'), (b'AMP', b'Amplificateur'), (b'CAB', b'C\xc3\xa2ble'), (b'SUP', b'Support'), (b'MIX', b'Table de mixage'), (b'JEU', b"Jeux d'orgue")]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Sous_Cat_Matos',
        ),
    ]
