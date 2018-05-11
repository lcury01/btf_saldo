# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0010_table_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_temp',
            name='nome2',
        ),
        migrations.AddField(
            model_name='table_temp',
            name='nome2',
            field=models.ManyToManyField(to='btf_saldo.CadastroAUX'),
        ),
    ]
