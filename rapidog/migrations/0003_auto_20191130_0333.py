# Generated by Django 2.2.7 on 2019-11-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidog', '0002_auto_20191130_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
