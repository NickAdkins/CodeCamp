# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0002_phase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]
