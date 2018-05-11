# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0007_auto_20180502_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talento',
            name='descricao',
            field=models.TextField(max_length=1000, verbose_name='seu Talento', help_text='Descreva como vc quer oferecer seu talento ao grupo BTF'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='experiencia',
            field=models.TextField(max_length=1000, verbose_name='experiência', help_text='Nos conte qual a sua experiência com esse talento. Isso fica apenas nos nossos registros, para ações maiores do BTF, quando precisarmos de talentos bem especificos nos eventos em grupo ou projetos sociais'),
        ),
        migrations.RemoveField(
            model_name='talento',
            name='quem',
        ),
        migrations.AddField(
            model_name='talento',
            name='quem',
            field=models.ManyToManyField(to='btf_saldo.Cadastro'),
        ),
        migrations.AlterField(
            model_name='talento',
            name='regiao',
            field=models.ForeignKey(on_delete=models.CASCADE, to='btf_saldo.Regiao', verbose_name='Região de Atuação', help_text='Regiao onde vc pode ajudar com seu talento'),
        ),
    ]
