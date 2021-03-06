# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170330_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('w', 'withdrawn')], default='draft', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, help_text='Optional 입니다.', max_length=100),
        ),
    ]
