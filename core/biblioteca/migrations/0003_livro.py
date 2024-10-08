# Generated by Django 5.0.7 on 2024-08-04 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_categoria'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_lancamento', models.DateField()),
                ('disponivel', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='biblioteca.autores')),
                ('capa', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.categoria')),
                ('generos', models.ManyToManyField(to='biblioteca.generos')),
            ],
        ),
    ]
