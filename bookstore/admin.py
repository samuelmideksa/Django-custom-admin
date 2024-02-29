from django.contrib import admin
from bookstore.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ['name']


admin.site.register(Book)