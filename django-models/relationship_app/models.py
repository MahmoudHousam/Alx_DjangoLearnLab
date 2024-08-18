from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library)

    def __str__(self):
        return self.name
