# Generated by Django 5.0.7 on 2024-09-11 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_alter_usuario_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='account_type',
        ),
    ]
