from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField()


class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author)


class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library)
