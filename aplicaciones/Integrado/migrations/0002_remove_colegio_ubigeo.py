# Generated by Django 4.2.5 on 2023-09-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Integrado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colegio',
            name='ubigeo',
        ),
    ]
