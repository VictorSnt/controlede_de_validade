# Generated by Django 4.0 on 2024-02-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_control', '0009_delete_alterdatadocprods_delete_alterdatadocs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comissao',
            old_name='cdprincipal',
            new_name='produto',
        ),
    ]
