from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("title", "author")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)
