# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0009_auto_20180507_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Temp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome2', models.TextField(max_length=100)),
                ('nome1', models.ForeignKey(to='btf_saldo.Cadastro',on_delete=models.CASCADE)),
            ],
        ),
    ]
