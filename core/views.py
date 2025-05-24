from django.shortcuts import render ,redirect
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def details(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, "details.html", {'book': book})

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
        username = request.post['username']
        password = request.post['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('books.html')
    return render(request, 'login.html')
