from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.core.paginator import Paginator


def index(request):
    return redirect('admin')


def admin(request):
    context = {}
    authors_count = Author.objects.count()
    context['authors_count'] = authors_count
    books_count = Book.objects.count()
    context['books_count'] = books_count

    return render(request, 'admin.html', context)


def view_authors(request):
    context = {}
    authors = Author.objects.all()
    paginator = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            author = Author.objects.get(id=pk)

            # to delete books written only by the author
            author_books = Book.objects.filter(authors=author)
            for author_book in author_books:
                if author_book.authors.count() == 1:
                    author_book.delete()

            author.delete()
            # Redirect to the same page after deletion
            return redirect('view_authors' + ('?page=' + page_number if page_number else ''))

    return render(request, 'view_authors.html', context)


def add_author(request):
    context = {}
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_authors')
    else:
        form = AuthorForm()
    context['form'] = form
    return render(request, 'add_author.html', context)


def edit_author(request, author_id):
    context = {}
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = AuthorForm(request.POST, request.FILES, instance=author)
            form.save()
            return redirect('view_authors')
        elif 'delete' in request.POST:
            author.delete()
            return redirect('view_authors')
    else:
        form = AuthorForm(instance=author)
        context['form'] = form
    return render(request, 'edit_author.html', context)


def view_books(request):
    context = {}
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj

    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            book = Book.objects.get(id=pk)
            book.delete()
            # Redirect to the same page after deletion
            return redirect('view_books' + ('?page=' + page_number if page_number else ''))

    return render(request, 'view_books.html', context)


def add_book(request):
    context = {}
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
        context['form'] = form
        context['authors'] = Author.objects.all()
        return render(request, 'add_book.html', context)


def edit_book(request, book_id):
    context = {}
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('view_books')
        elif 'delete' in request.POST:
            book.delete()
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
        context['form'] = form
    return render(request, 'edit_book.html', context)
