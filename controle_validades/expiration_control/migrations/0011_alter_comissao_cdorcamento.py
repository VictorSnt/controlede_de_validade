# Generated by Django 4.0 on 2024-02-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_control', '0010_rename_cdprincipal_comissao_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='cdorcamento',
            field=models.CharField(max_length=20),
        ),
    ]
