# Generated by Django 5.0.7 on 2024-09-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_remove_usuario_age_remove_usuario_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='has_book',
            field=models.BooleanField(default=False),
        ),
    ]
