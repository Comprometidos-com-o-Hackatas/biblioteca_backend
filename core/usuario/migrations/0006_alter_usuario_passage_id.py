# Generated by Django 5.0.7 on 2024-09-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_usuario_passage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='passage_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
