# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20150210_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_matos',
            name='categorie',
            field=models.CharField(max_length=16, verbose_name=b'cat\xc3\xa9gorie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sous_cat_matos',
            name='sous_categorie',
            field=models.CharField(max_length=16, verbose_name=b'sous-cat\xc3\xa9gorie'),
            preserve_default=True,
        ),
    ]
