# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20150208_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_Matos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categorie', models.CharField(max_length=3, verbose_name=b'cat\xc3\xa9gorie', choices=[(b'LUM', b'Lumi\xc3\xa8re'), (b'SON', b'Son'), (b'VID', b'Vid\xc3\xa9o'), (b'MAC', b'Machinerie'), (b'ADM', b'Administratif'), (b'IND', b'Ind\xc3\xa9termin\xc3\xa9')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sous_Cat_Matos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sous_categorie', models.CharField(max_length=4, verbose_name=b'sous-cat\xc3\xa9gorie', choices=[(b'PROJ', b'Projecteur'), (b'DIMM', b'Dimmer'), (b'ORGU', b"Jeux d'orgue"), (b'ENCE', b'Enceinte'), (b'MICR', b'Microphone'), (b'AMPL', b'Amplification'), (b'PROC', b'Processing'), (b'MIXE', b'Table de mixage'), (b'CABL', b'C\xc3\xa2blage'), (b'VIDP', b'Vid\xc3\xa9o Projecteur'), (b'LEVA', b'Levage'), (b'TISS', b'Tissu'), (b'SUPP', b'Support'), (b'UNKN', b'Ind\xc3\xa9termin\xc3\xa9'), (b'none', b'Veuillez choisir une sous-cat\xc3\xa9gorie')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='matos',
            name='categorie',
            field=models.ForeignKey(verbose_name=b'cat\xc3\xa9gorie', to='stock.Cat_Matos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='sous_categorie',
            field=models.ForeignKey(verbose_name=b'sous-cat\xc3\xa9gorie', to='stock.Sous_Cat_Matos'),
            preserve_default=True,
        ),
    ]
