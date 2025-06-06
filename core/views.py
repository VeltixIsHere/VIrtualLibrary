from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import RegisterForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


@login_required(login_url='login')
def details(request, pk):
    book = get_object_or_404(Book, id=pk)
    comments = book.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.book = book
            comment.save()
            return redirect('details', book_id=book.id)
    return render(request, "details.html", {'book': book, 'comments': comments, 'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('books')
    return render(request, 'login.html')
