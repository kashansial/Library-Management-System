from django.db import models

# Create your models here.

    
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name
    
class Author(models.Model):
    auth_id = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=100)

    def __str__(self):
        return self.auth_name
    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='book_cover/', null=True, blank=True)  
    book_title = models.CharField(max_length=200)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.book_title
    
