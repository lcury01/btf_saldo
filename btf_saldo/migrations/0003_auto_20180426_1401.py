# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-26 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0002_auto_20180423_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='descreva seu talento')),
                ('experiencia', models.CharField(max_length=100, verbose_name='descreva seu talento')),
                ('quem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.Cadastro', verbose_name='Associado')),
            ],
        ),
        migrations.CreateModel(
            name='TalentoClasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Qual a área do Talento')),
            ],
        ),
        migrations.AddField(
            model_name='talento',
            name='talentoclasse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.TalentoClasse', verbose_name='area do talento'),
        ),
    ]
