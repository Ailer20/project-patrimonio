# Generated by Django 5.2 on 2025-04-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0002_controlechaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlechaves',
            name='situacao',
            field=models.CharField(default='RETIRADO', max_length=100, null=True),
        ),
    ]
