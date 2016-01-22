# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Назва')),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=256, verbose_name='Прізвище')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='По-батькові')),
                ('birthday', models.DateField(verbose_name='Дата народження', null=True)),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фото', null=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='Білет')),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
                ('student_group', models.ForeignKey(to='students.Group', null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Група')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(to='students.Student', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Староста'),
        ),
    ]
