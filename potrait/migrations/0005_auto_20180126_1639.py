# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potrait', '0004_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(to='potrait.Category'),
        ),
    ]
