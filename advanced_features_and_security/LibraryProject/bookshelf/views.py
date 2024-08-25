
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from django.http import HttpResponse

@permission_required('bookshelf.can_create', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            document = Document.objects.create(title=title, content=content, author=request.user)
            return redirect('document_list')
        else:
            return render(request, 'bookshelf\create_document.html', {'error': 'All fields are required.'})
    return render(request, 'bookshelf/create_document.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()
        return redirect('bookshelf/edit_document.html', pk=document.pk)
    return render(request, 'bookshelf/edit_document.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'bookshelf/delete_document.html', {'document': document})

@permission_required('bookshelf.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})
