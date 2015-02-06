# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_auto_20150131_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(verbose_name='provider', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(verbose_name='provider', max_length=30),
            preserve_default=True,
        ),
    ]
