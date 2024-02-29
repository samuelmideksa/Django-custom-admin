from django.db import models
from django.core.exceptions import ValidationError


def validate_isbn(value):
    if not (value.isdigit() and (len(value) == 10 or len(value) == 13)):
        raise ValidationError('Invalid ISBN format')


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    cover_image = models.ImageField(upload_to='')
    rating = models.FloatField()
    genres = models.CharField(max_length=200, null=True, blank=True)
    isbn = models.CharField(max_length=13, validators=[validate_isbn], null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    publisher = models.TextField(max_length=100)
    published_date = models.DateField()
    languages = models.CharField(max_length=200, null=True, blank=True)
    plot = models.TextField(null=True, blank=True)

    def author_list(self):
        return list(author.name for author in self.authors.all())

    def __str__(self):
        return self.title
