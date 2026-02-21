from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('register/', views.Registeration, name='registeration'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('logout/', views.logout_view, name='logout'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/reserve/', views.reserve_book, name='reserve_book_action'),
]