from django.shortcuts import render


from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library




def FunctionView(request):
    books = Book.objects.all()
    response_content = "<h1>Books Available:</h1><ul>"
    for book in books:
        response_content += f"<li>{book.name} by {book.author.name}</li>"
    response_content += "</ul>"
    return HttpResponse(response_content)



class ClassView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
