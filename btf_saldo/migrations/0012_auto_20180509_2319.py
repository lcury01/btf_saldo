# Generated by Django 2.0.5 on 2018-05-10 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btf_saldo', '0011_auto_20180508_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_temp',
            name='nome2',
        ),
        migrations.AddField(
            model_name='table_temp',
            name='nome2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='btf_saldo.CadastroAUX'),
            preserve_default=False,
        ),
    ]
