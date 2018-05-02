# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0005_auto_20180430_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento2',
            name='credito_fk',
            field=models.ForeignKey(to='btf_saldo.CadastroAUX', verbose_name='quem recebe os créditos'),
        ),
        migrations.AlterField(
            model_name='lancamento2',
            name='debito_fk',
            field=models.ForeignKey(to='btf_saldo.Cadastro', verbose_name='qum transfere os creditos'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='descricao',
            field=models.CharField(max_length=1000, verbose_name='descreva seu talento'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='experiencia',
            field=models.CharField(max_length=1000, verbose_name='sua experiência'),
        ),
    ]
