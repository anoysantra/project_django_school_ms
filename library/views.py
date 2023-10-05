from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Library
from .forms import LibraryForm

def add_book(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = LibraryForm()
    return render(request, 'add_book.html', {'form': form})


def list_book(request):
    books = Library.objects.all()
    return render(request, 'list_book.html', {'books': books})


def update_book(request, book_id):
    book = get_object_or_404(Library, book_id=book_id)
    val_check=book.book_id

    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=book)

        if form.is_valid():
            book_id_check=form.cleaned_data['book_id']

            if val_check != book_id_check:
                print("Check Condition")
                return HttpResponse("<h1>Update of Id not allowed. Create a new one with Specified Id")
            
            form.save()
            return redirect('list_book')
    else:
        form = LibraryForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Library, book_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_book')
    return render(request, 'delete_book.html', {'book': book})

