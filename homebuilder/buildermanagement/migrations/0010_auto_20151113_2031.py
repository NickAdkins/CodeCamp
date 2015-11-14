# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='plansfile',
            field=models.FileField(upload_to=b'files/%Y/%m/%d', null=True, verbose_name=b'Plans file', blank=True),
        ),
    ]
