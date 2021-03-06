# Generated by Django 2.2.8 on 2019-12-06 04:31

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidog', '0011_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nome_produto', unique_with=('codigo_produto',)),
        ),
    ]
