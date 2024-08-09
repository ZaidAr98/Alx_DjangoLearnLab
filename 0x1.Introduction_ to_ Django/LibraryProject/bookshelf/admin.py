
# Register your models here.
from django.contrib import admin
from bookshelf.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author','publication_year')

admin.site.register(Book, BookAdmin)