from django.shortcuts import render, redirect, get_object_or_404
from core.models import Student
from books.models import Book, Category
from .models import IssuedBooks
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import timedelta
from django.utils import timezone

def Registeration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if Student.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken.")
        elif Student.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
        else:
         new_student = Student.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone=phone # Extra field from your AbstractUser
            )
         messages.success(request, "Registration successful! Please login.")
        return redirect('dashboard:login') 

    return render(request, 'dashboard/registeration.html', {'page_title': 'Sign Up'})

def login_view(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('dashboard:login')
   return render(request, 'dashboard/login.html', {'page_title': 'Login'})

@login_required 
def dashboard_home(request):
    # ADD .select_related('book') to avoid slow page loads
    my_books = IssuedBooks.objects.filter(student=request.user).select_related('book', 'book__book_author')
    
    context = {
        'page_title': 'Student Dashboard',
        'my_books': my_books,
    }
    return render(request, 'dashboard/dashboard_home.html', context)

def logout_view(request):
    logout(request)
    return redirect('dashboard:login')


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'dashboard/book_details.html', {'book': book})

def reserve_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=book_id)
        
        # Create the IssuedBooks entry
        IssuedBooks.objects.create(
            student=request.user,
            book=book,
            # Setting a default return date (e.g., 14 days from now)
            return_date=timezone.now().date() + timedelta(days=14)
        )
        return redirect('dashboard:dashboard_home')