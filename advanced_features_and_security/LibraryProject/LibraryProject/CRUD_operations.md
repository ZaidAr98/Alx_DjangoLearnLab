from bookshelf.models import Book

new_book = Book.objects.create(title="1984", author="George Orwell",publication_year=1949)
new_book.save()


from bookshelf.models import Book

retrieved_book = Book.objects.get(title="1984")

print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")



# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949


retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()




updated_book.delete()