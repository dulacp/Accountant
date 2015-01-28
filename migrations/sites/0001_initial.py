# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.sites.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('domain', models.CharField(validators=[django.contrib.sites.models._simple_domain_name_validator], max_length=100, verbose_name='domain name')),
                ('name', models.CharField(max_length=50, verbose_name='display name')),
            ],
            options={
                'db_table': 'django_site',
                'verbose_name': 'site',
                'verbose_name_plural': 'sites',
                'ordering': ('domain',),
            },
            bases=(models.Model,),
        ),
    ]
