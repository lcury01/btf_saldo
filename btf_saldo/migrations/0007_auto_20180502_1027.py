# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0006_auto_20180502_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talento',
            name='descricao',
            field=models.CharField(help_text='descreva como vc quer oferecer seu talento ao grupo BTF', max_length=1000, verbose_name='seu Talento'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='experiencia',
            field=models.CharField(help_text='nos conte qual a sua experiência com esse talento', max_length=1000, verbose_name='experiência'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='quem',
            field=models.ForeignKey(on_delete=models.CASCADE,help_text='Quem é você no BTF? Seu nome igual ao da planilha de créditos', to='btf_saldo.Cadastro', verbose_name='Associado'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='regiao',
            field=models.ForeignKey(on_delete=models.CASCADE,help_text='regiao onde vc pode ajudar com seu talento', to='btf_saldo.Regiao', verbose_name='Região de Atuação'),
        ),
    ]
