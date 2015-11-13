# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildermanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('order_by', models.DateTimeField()),
                ('contact', models.ForeignKey(to='buildermanagement.Contact')),
                ('depends_on', models.ForeignKey(blank=True, to='buildermanagement.Phase', null=True)),
            ],
        ),
    ]
