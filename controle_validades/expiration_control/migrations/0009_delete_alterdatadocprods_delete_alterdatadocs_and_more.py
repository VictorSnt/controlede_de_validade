# Generated by Django 4.0 on 2024-02-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_control', '0008_rename_altedatadocs_alterdatadocs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AlterdataDocProds',
        ),
        migrations.DeleteModel(
            name='AlterdataDocs',
        ),
        migrations.DeleteModel(
            name='AlterdataProds',
        ),
    ]