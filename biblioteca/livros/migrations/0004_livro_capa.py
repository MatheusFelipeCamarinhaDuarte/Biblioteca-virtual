# Generated by Django 5.0.6 on 2024-07-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_livro_emprestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, upload_to='capas/%d/%m/%Y'),
        ),
    ]
