# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0008_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phase',
            options={'ordering': ['start_date', 'completed']},
        ),
        migrations.RemoveField(
            model_name='phase',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='order_by',
        ),
        migrations.AddField(
            model_name='phase',
            name='order_materials_by',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='phase',
            name='project',
            field=models.ForeignKey(default=1, to='buildermanagement.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='plansfile',
            field=models.FileField(upload_to=b'files/%Y/%m/%d', null=True, verbose_name=b'Plans file', blank=True),
        ),
    ]
