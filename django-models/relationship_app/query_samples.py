from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = 'Zaid'
author = Author.objects.filter(name=author_name)
books_by_author = Book.objects.filter(author=author) # using related_name 'books'

for book in books_by_author:
    print(book.name)

# List all books in a library
library_name = 'Khartoum'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  # using related_name 'books'

for book in books_in_library:
    print(book.name)

# Retrieve the librarian for a library
library_name = 'Mohamed'
librarian = Librarian.objects.get(library__name=library_name)
print(f"Librarian of {library_name}: {librarian.name}")
