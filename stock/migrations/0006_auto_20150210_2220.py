# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20150210_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matos',
            name='date_ajout',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b"Date d'ajout"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matos',
            name='date_modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Date de modification'),
            preserve_default=True,
        ),
    ]
