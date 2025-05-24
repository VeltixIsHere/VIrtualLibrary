from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book


# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def details(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, "details.html", {'book': book})
