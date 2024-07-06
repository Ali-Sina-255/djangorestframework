from django.urls import path
from . import views


urlpatterns = [
    path("", views.AuthorListApiView.as_view(), name="author-list"),
    path("<int:pk>/", views.AuthorDetailApiView.as_view(), name="author-detail"),
    path("books/", views.BookListApiView.as_view(), name="book-list"),
    path("<int:pk>/", views.BookDetailApiView.as_view(), name="book-detail"),
]

# urlpatterns = [
#     path("books/", views.BookApiLitView.as_view(), name='book-list'),
#     path("book/", views.book_list_api_view, name='book-list'),
#     path("author/", views.author_list_api_view, name='author-list'),
# ]
