from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('library:category-detail', kwargs={'pk': self.pk })


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    book_detail = models.TextField(max_length=5000, default='Details not available')
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('library:book-detail', kwargs={'pk': self.pk})
