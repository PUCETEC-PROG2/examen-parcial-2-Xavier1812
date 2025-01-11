from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    
    MOVIE_GENRES = [
        ('Action', 'Accion'),
        ('SciFi', 'Ciencia Ficcion'),
        ('Comedy', 'Comedia'),
        ('Documental', 'Documental'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasia'),
    ]
    genre = models.CharField(max_length=30, null=False, choices=MOVIE_GENRES)
    movie_director = models.CharField(max_length=50, null=False)
    publication_year = models.DateField()
    sinopsis = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='movie_images')
    
    def __str__(self):
        return f'{self.title} - {self.publication_year}'