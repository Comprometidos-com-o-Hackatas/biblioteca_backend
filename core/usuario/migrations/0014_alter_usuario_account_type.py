# Generated by Django 5.0.7 on 2024-09-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_usuario_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='account_type',
            field=models.IntegerField(choices=[(1, 'ADULTO'), (2, 'INFANTOJUVENIL'), (3, 'INFANTIL')], default=1),
        ),
    ]
