# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=200)),
                ('name_image', models.CharField(max_length=200)),
                ('id_container', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('virual_size', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('id_images', models.CharField(max_length=200)),
                ('virtual_size', models.CharField(max_length=200)),
                ('repo_tags', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pushed_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('id_images', models.CharField(max_length=200)),
                ('virtual_size', models.CharField(max_length=200)),
                ('repo_tags', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('id_images', models.CharField(max_length=200)),
                ('virtual_size', models.CharField(max_length=200)),
                ('repo_tags', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('cmd', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
