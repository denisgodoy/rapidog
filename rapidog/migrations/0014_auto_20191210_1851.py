# Generated by Django 2.2.8 on 2019-12-10 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidog', '0013_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
