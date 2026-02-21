from django.db import models
from books.models import  Book
from django.conf import settings

# Create your models here.

class IssuedBooks(models.Model):
    issue_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.book.book_title}"