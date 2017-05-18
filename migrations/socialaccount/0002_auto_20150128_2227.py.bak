# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import allauth.socialaccount.fields


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='extra_data',
            field=allauth.socialaccount.fields.JSONField(default='{}', verbose_name='extra data'),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(verbose_name='provider', max_length=30),
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(verbose_name='provider', max_length=30),
        ),
    ]
