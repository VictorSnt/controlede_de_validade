# Generated by Django 4.0 on 2024-01-27 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_control', '0003_detalhe_alterdatadetalhe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='AlterdataDetalhe',
        ),
    ]
