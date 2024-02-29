from django import forms
from .models import Author, Book


# creating a form
class AuthorForm(forms.ModelForm):
    # create meta_class
    class Meta:
        # specify model to be used
        model = Author

        # specify fields to be used
        fields = ['name','image','bio']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'cover_image',
            'rating',
            'genres',
            'isbn',
            'publisher',
            'published_date',
            'languages',
            'plot',
        ]
        widgets = {
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'languages': forms.TextInput(attrs={'class': 'form-control'}),
            'plot': forms.Textarea(attrs={'class': 'form-control'}),
        }
