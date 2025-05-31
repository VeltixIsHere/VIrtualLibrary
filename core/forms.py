from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class BookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-title'}), max_length=50)
    cover = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-cover'}), max_length=50)
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-image'}), max_length=255)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


