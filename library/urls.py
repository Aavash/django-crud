from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book-list/', views.BookListView.as_view(), name='book-list'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book-create/', views.BookCreateView.as_view(), name='book-create'),
    path('book-update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),

    path('category-list/', views.CategoryListView.as_view(), name='category-list'),
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category-create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
]