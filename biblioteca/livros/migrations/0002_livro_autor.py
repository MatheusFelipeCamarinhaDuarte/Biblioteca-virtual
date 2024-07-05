# Generated by Django 5.0.6 on 2024-07-05 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='autores.autor'),
            preserve_default=False,
        ),
    ]
