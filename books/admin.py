from django.contrib import admin
from .models import Category, Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # This makes the admin look like a real table with columns
    list_display = ('book_title', 'book_author', 'book_category', 'book_isbn')
    search_fields = ('book_title', 'book_isbn') # Adds a search bar
    list_filter = ('book_category',) # Adds a filter sidebar

admin.site.register(Category)
admin.site.register(Author)