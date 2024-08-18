from django.db import models
from django.contrib.auth.models import User


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


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title
