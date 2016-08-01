# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-07-29 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_list', '0003_auto_20160729_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('lasttouch', models.CharField(max_length=50)),
                ('nexttouch', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contactlist',
            },
        ),
        migrations.RemoveField(
            model_name='dreamreal',
            name='online',
        ),
        migrations.DeleteModel(
            name='Dreamreal',
        ),
        migrations.DeleteModel(
            name='Online',
        ),
    ]
