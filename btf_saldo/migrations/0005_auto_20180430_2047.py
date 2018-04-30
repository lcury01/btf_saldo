# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0004_auto_20180426_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento2',
            name='credito_fk',
            field=models.CharField(verbose_name='Nome do Associado2', max_length=50),
        ),
        migrations.AlterField(
            model_name='lancamento2',
            name='debito_fk',
            field=models.CharField(verbose_name='Nome do Associado', max_length=50),
        ),
        migrations.AlterField(
            model_name='talento',
            name='experiencia',
            field=models.CharField(verbose_name='sua experiência', max_length=100),
        ),
    ]
