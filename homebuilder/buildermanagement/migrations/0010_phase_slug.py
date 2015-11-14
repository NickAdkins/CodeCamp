# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0009_auto_20151113_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]
