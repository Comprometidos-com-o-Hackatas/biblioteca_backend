# Generated by Django 5.0.7 on 2024-09-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_remove_usuario_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
