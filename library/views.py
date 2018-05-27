from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView
from .models import Category, Book


class HomeView(TemplateView):
    template_name = 'library/home.html'


# Book
class BookCreateView(CreateView):
    model = Book
    template_name = 'forms/book_form.html'
    fields = ['category', 'book_name', 'author', 'book_detail']


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'forms/book_form.html'
    fields = ['category', 'book_name', 'author', 'book_detail', 'borrowed']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'forms/book_confirm_delete.html'
    success_url = reverse_lazy('library:book-list')


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book_detail'

    # def get_queryset(self):
    #     return Book.objects.filter(id=self.pk)


# Category
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'forms/category_form.html'
    fields = ['category_name']


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'forms/category_form.html'
    fields = ['category_name']


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'forms/category_confirm_delete.html'
    success_url = reverse_lazy('library:category-list')


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category_detail'

