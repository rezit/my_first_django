# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0012_remove_quran_gambar'),
    ]

    operations = [
        migrations.AddField(
            model_name='quran',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]