# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0008_auto_20180507_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talento',
            name='quem',
        ),
        migrations.AddField(
            model_name='talento',
            name='quem',
            field=models.ForeignKey(to='btf_saldo.Cadastro', default=1),
            preserve_default=False,
        ),
    ]
