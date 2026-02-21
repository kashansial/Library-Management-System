from django.shortcuts import render, get_object_or_404
from .models import Book, Category, Author
from django.core.paginator import Paginator

def home(request):
    books_list = Book.objects.select_related('book_author', 'book_category').all()
    paginator = Paginator(books_list, 12)  # 12 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/index.html', {
        'books': page_obj,
        'page_title': "Explore Books"
    })

def book_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    author_id = request.GET.get('author')
    # 1. First, tell Django WHICH tables to join (book_author and book_category)
    books_list = Book.objects.select_related('book_author', 'book_category').all()
    
    # 2. Second, apply the FILTER if a category was selected
    if category_id:
        # Note: Use book_category_id (the field name) = category_id (your variable)
        books_list = books_list.filter(book_category_id=category_id)
    
    if author_id:
        books_list = books_list.filter(book_author_id=author_id)
    # 3. Finally, Paginate
    paginator = Paginator(books_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {
        'books': page_obj,
        'categories': categories,
    })
def categories_view(request):
    # Fetch all categories and count how many books are in each
    categories = Category.objects.all()
    return render(request, 'books/categories.html', {'categories': categories})
   

def auth_dashboard(request):
    authors = Author.objects.all().order_by('auth_name')
    return render(request,'books/author_dashboard.html',{ 
    'authors' : authors})

def author_books(request, auth_id):
    author = get_object_or_404(Author, auth_id=auth_id)

    books = Book.objects.filter(book_auth=author)
    context = {
        'author': author,
        'books':books
    }
    return render(request, 'books/auth_books.html',context)
