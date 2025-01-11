# Generated by Django 5.1.4 on 2025-01-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Action', 'Accion'), ('SciFi', 'Ciencia Ficcion'), ('Comedy', 'Comedia'), ('Documental', 'Documental'), ('Drama', 'Drama'), ('Fantasy', 'Fantasia')], max_length=30)),
                ('movie_director', models.CharField(max_length=50)),
                ('publication_year', models.DateField()),
                ('sinopsis', models.TextField(max_length=500)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
