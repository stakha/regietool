# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20150208_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matos',
            name='link',
        ),
        migrations.AddField(
            model_name='matos',
            name='directivite',
            field=models.CharField(blank=True, max_length=3, verbose_name=b'directivit\xc3\xa9', choices=[(b'OMN', b'Omnidirectionnel'), (b'CAR', b'Cardio\xc3\xafde'), (b'HYP', b'HyperCardio\xc3\xafde'), (b'CAN', b'Canon')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='sensibilite',
            field=models.DecimalField(decimal_places=2, max_digits=4, blank=True, help_text=b'En mV/Pa', null=True, verbose_name=b'sensibilit\xc3\xa9'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matos',
            name='type_micro',
            field=models.CharField(blank=True, max_length=3, verbose_name=b'type de micro', choices=[(b'DYN', b'Micro dynamique'), (b'CON', b'Micro \xc3\xa0 condensateur'), (b'RUB', b'Micro \xc3\xa0 ruban')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='categorie',
            field=models.CharField(default=b'unknown', max_length=12, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'lumi\xc3\xa8re', b'Lumi\xc3\xa8re'), (b'son', b'Son'), (b'video', b'Vid\xc3\xa9o'), (b'machinerie', b'Machinerie'), (b'unknown', b'Ind\xc3\xa9termin\xc3\xa9')]),
            preserve_default=True,
        ),
    ]
