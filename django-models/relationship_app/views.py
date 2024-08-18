from django.shortcuts import render


from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library




def FunctionView(request):
     books = Book.objects.all()
    return render(request, 'relationship_app/templates/list_books.html', {'books': books})



class ClassView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
