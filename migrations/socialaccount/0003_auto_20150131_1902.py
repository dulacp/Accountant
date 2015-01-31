# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0002_auto_20150128_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(verbose_name='provider', choices=[('facebook', 'Facebook'), ('github', 'GitHub'), ('twitter', 'Twitter')], max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(verbose_name='provider', choices=[('facebook', 'Facebook'), ('github', 'GitHub'), ('twitter', 'Twitter')], max_length=30),
            preserve_default=True,
        ),
    ]
