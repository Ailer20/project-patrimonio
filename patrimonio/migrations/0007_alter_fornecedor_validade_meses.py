# Generated by Django 5.2 on 2025-05-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0006_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='validade_meses',
            field=models.IntegerField(),
        ),
    ]
