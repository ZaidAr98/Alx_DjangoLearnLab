from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = 'Zaid'
books_by_author = Book.objects.filter(author=author)




# List all books in a library
library_name = 'Khartoum'
library = Library.objects.filter(name=library_name)



# Retrieve the librarian for a library
library_name = 'Mohamed'
librarian = Librarian.objects.filter(library__name=library_name)

