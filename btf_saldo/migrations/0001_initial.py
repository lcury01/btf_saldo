# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-23 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Associado')),
                ('conta', models.CharField(max_length=7, verbose_name='Conta BTF')),
                ('saldo_inicial', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Saldo Inicial em Creditos de Tempo')),
            ],
        ),
        migrations.CreateModel(
            name='CadastroAUX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Associado')),
                ('conta', models.CharField(max_length=7, verbose_name='Conta BTF')),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Qual foi a troca')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Créditos de Tempo')),
                ('credito_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.CadastroAUX', verbose_name='quem recebe os créditos')),
                ('debito_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.Cadastro', verbose_name='quem transfere os créditos')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Qual foi a troca')),
                ('comquem', models.CharField(default='', max_length=50, verbose_name='Com que trocou')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Créditos de Tempo')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da Transferência')),
                ('sinal', models.CharField(max_length=1, verbose_name='Sinal')),
                ('quem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.Cadastro')),
            ],
        ),
    ]
