# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
