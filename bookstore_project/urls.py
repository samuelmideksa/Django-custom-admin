"""
URL configuration for bookstore_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from bookstore.views import add_author, edit_author, view_authors, view_books, add_book, edit_book, admin, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', index),
                  path('admin/', admin, name='admin'),
                  path('admin/authors/', view_authors, name='view_authors'),
                  path('admin/authors/add-author/', add_author, name='add_author'),
                  path('admin/authors/edit-author/<int:author_id>/', edit_author, name='edit_author'),
                  path('admin/books/', view_books, name='view_books'),
                  path('admin/books/add-book/', add_book, name='add_book'),
                  path('admin/books/edit-book/<int:book_id>/', edit_book, name='edit_book'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
