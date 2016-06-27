# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('full_name', models.CharField(max_length=255, verbose_name=b'full name', blank=True)),
                ('preferred_name', models.CharField(max_length=255, verbose_name=b'preferred name', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
