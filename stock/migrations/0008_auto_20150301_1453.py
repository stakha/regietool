# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20150215_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matos',
            name='categorie',
            field=models.CharField(max_length=3, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'lum', b'Lumi\xc3\xa8re'), (b'son', b'Son'), (b'vid', b'Vid\xc3\xa9o'), (b'pla', b'Plateau')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='nom',
            field=models.CharField(max_length=50, verbose_name=b'nom usuel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='sous_categorie',
            field=models.CharField(max_length=3, verbose_name=b'sous cat\xc3\xa9gorie', choices=[(b'None', b'---------'), (b'Lumi\xc3\xa8re', ((b'pro', b'Projecteur'), (b'pup', b"Jeux d'orgue"), (b'dim', b'Gradateur'))), (b'Son', ((b'enc', b'Enceinte'), (b'mic', b'Microphone'), (b'amp', b'Amplificateur'), (b'mix', b'Table de mixage'), (b'pro', b'Processing'))), (b'Vid\xc3\xa9o', ((b'vip', b'Vid\xc3\xa9o projecteur'),)), (b'cab', b'C\xc3\xa2ble'), (b'sup', b'Support')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='type_micro',
            field=models.CharField(blank=True, max_length=21, verbose_name=b'type de micro', choices=[('Micro dynamique', b'Micro dynamique'), ('Micro \xe0 condensateur', b'Micro \xc3\xa0 condensateur'), ('Micro \xe0 ruban', b'Micro \xc3\xa0 ruban')]),
            preserve_default=True,
        ),
    ]
