from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookApiLitView.as_view(), name='book-list'),
    path("book/", views.book_list_api_view, name='book-list'),
    path("author/", views.author_list_api_view, name='author-list'),
]
