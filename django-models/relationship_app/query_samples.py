from .models import Author, Book, Library, Librarian

# Add Author objects
nageeb = Author.objects.create(name="Nageeb Mahfouz")
nageeb.save()
ehsan = Author.objects.create(name="Ehsan Abdelkkodos")
ehsan.save()
author_name = Author.objects.create(name="Author Name")

# Add Book objects
cairo_30 = Book.objects.create(title="Cairo 30", author=nageeb)
arabisk = Book.objects.create(title="Arabisk", author=ehsan)

cairo_30.save()
arabisk.save()

# Get books by one author
Book.objects.get(author=ehsan)
Book.objects.get(author=nageeb)
Author.objects.get(name=author_name)
Author.objects.filter(author=author)

# List all books
Book.objects.all()

# Create Library Instance
grow = Library.objects.create(name="grow")
grow.save()

# Add books to Library
grow.books.add(cairo_30, arabisk)

# List all books in Library
grow.books.all()
# Library.objects.get(name=library_name)

# Add Librarian
agyim = Librarian.objects.create(name="Agyim Taala", library=grow)
agyim.save()

# Retrieve a Libryrian for a library
agyim.library
Librarian.objects.get(library=grow)
