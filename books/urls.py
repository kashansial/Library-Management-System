from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
path('', views.book_list, name='book_list'),
path('books/', views.book_list, name='book_list'),
path('categories/', views.categories_view, name='category_list'),
path('authors/', views.auth_dashboard, name='author_dashboard'),
path('authors/<int:auth_id>/', views.author_books, name='author_books'),
]
