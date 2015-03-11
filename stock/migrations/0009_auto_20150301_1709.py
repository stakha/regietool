# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20150301_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='matos',
            name='angle_max',
            field=models.IntegerField(help_text=b'En degr\xc3\xa9s', max_length=3, null=True, verbose_name=b'angle maximum', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='angle_min',
            field=models.IntegerField(help_text=b'En degr\xc3\xa9s', max_length=3, null=True, verbose_name=b'angle minimum', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='has_dmx',
            field=models.NullBooleanField(verbose_name=b'DMX'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='puissance_proj',
            field=models.IntegerField(help_text=b'En watts', max_length=5, null=True, verbose_name=b'puissance', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='tension_proj',
            field=models.IntegerField(help_text=b'En volts', max_length=3, null=True, verbose_name=b'tension', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='type_proj',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name=b'type de projecteur', choices=[(b'Traditionnel', ((b'pc', b'Plan convexe'), (b'fre', b'Fresnel'), (b'dec', b'D\xc3\xa9coupe'), (b'par', b'PAR'), (b'qua', b'Quartz'), (b'bat', b'Basse tension'))), (b'Asservi', ((b'lyr', b'Lyre'), (b'pal', b'Par led'), (b'str', b'Stromboscope'))), (b'aut', b'Autre')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='sous_categorie',
            field=models.CharField(max_length=3, verbose_name=b'sous cat\xc3\xa9gorie', choices=[(b'Lumi\xc3\xa8re', ((b'prj', b'Projecteur'), (b'pup', b"Jeux d'orgue"), (b'dim', b'Gradateur'))), (b'Son', ((b'enc', b'Enceinte'), (b'mic', b'Microphone'), (b'amp', b'Amplificateur'), (b'mix', b'Table de mixage'), (b'prc', b'Processing'))), (b'Vid\xc3\xa9o', ((b'vip', b'Vid\xc3\xa9o projecteur'),)), (b'cab', b'C\xc3\xa2ble'), (b'sup', b'Support')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='type_micro',
            field=models.CharField(blank=True, max_length=21, verbose_name=b'type de micro', choices=[(b'DYN', b'Micro dynamique'), (b'CON', b'Micro \xc3\xa0 condensateur'), (b'RUB', b'Micro \xc3\xa0 ruban')]),
            preserve_default=True,
        ),
    ]
