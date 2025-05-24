from django import forms

class BookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-title'}), max_length=50)
    cover = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-cover'}), max_length=50)
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'book-image'}), max_length=255)


