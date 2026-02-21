from django.shortcuts import render
from .models import Student
from books.models import Book

def home(request):
    # .select_related improves performance by fetching related Author/Category data
    books = Book.objects.all().select_related('book_author', 'book_category')
    
    context = {
        'page_title': 'Library Management System',
        'books': books,
    }
    return render(request, 'core/home.html', context)