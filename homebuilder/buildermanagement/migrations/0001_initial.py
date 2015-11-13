# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_description', models.TextField(max_length=200)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_type', models.CharField(max_length=2, choices=[(b'sc', b'Subcontractor'), (b'hb', b'Home Builder'), (b'b', b'Buyer'), (b'v', b'Vendor')])),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('phone1', models.CharField(max_length=12, null=True, blank=True)),
                ('phone2', models.CharField(max_length=12, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=200)),
                ('cost', models.IntegerField()),
                ('picture', models.ImageField(null=True, upload_to=b'images/%Y/%m/%d', blank=True)),
                ('picture_url', models.URLField(null=True, blank=True)),
                ('estimate_needed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='buildermanagement.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('plansfile', models.FileField(null=True, upload_to=b'files/%Y/%m/%d', blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('budget', models.IntegerField(null=True, blank=True)),
                ('builder', models.ForeignKey(related_name='builder_set', to='buildermanagement.Contact')),
                ('buyer', models.ForeignKey(related_name='buyer_set', to='buildermanagement.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sqfootage', models.IntegerField()),
                ('project', models.ForeignKey(to='buildermanagement.Project')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='project',
            field=models.ForeignKey(to='buildermanagement.Project'),
        ),
        migrations.AddField(
            model_name='item',
            name='room',
            field=models.ManyToManyField(to='buildermanagement.Room'),
        ),
        migrations.AddField(
            model_name='contact',
            name='group',
            field=models.ForeignKey(blank=True, to='buildermanagement.Group', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='project',
            field=models.ForeignKey(to='buildermanagement.Project'),
        ),
        migrations.AddField(
            model_name='addon',
            name='item',
            field=models.ForeignKey(to='buildermanagement.Item'),
        ),
    ]
