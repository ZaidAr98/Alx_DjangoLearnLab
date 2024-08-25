from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse

@permission_required('your_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            book = Book.objects.create(title=title, content=content, author=request.user)
            return redirect('book_list')
        else:
            return render(request, 'your_app/create_book.html', {'error': 'All fields are required.'})
    return render(request, 'your_app/create_book.html')

@permission_required('your_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'your_app/edit_book.html', {'book': book})

@permission_required('your_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'your_app/delete_book.html', {'book': book})

@permission_required('your_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'your_app/book_list.html', {'books': books})
