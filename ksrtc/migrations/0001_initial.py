# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bustab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('busname', models.CharField(max_length=300)),
                ('Busid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='routetab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stops', models.CharField(max_length=300)),
                ('busob', models.ManyToManyField(to='ksrtc.bustab')),
            ],
        ),
    ]
