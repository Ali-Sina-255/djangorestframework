from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Books, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StudentPagination(LimitOffsetPagination):
    page_size = 2


class AuthorListApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'rating']


class AuthorDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = StudentPagination


class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = StudentPagination


# @api_view(["GET"])
# def author_list_api_view(request):
#     if request.method == "GET":
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data)


@api_view(["GET"])
def book_list_api_view(request):
    if request.method == "GET":
        author = request.objects.all()
        serializer = BookSerializer(author, many=True)
        return Response(serializer.data)


class AuthorListApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookApiLitView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


@api_view(["GET", "POST", "DELETE"])
def book_list_api_view(request):
    if request.method == "GET":
        author = Books.objects.all()
        serializer = BookSerializer(author, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST", "DELETE"])
def author_list_api_view(request):
    if request.method == "GET":
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# https://app.insomnia.rest/app/auth-app/?loginKey=tdiDAi2uZMOw%252FoyGsbhtnY9h0NvKjpK%252FYY5%252Bk6Qax0w%253D
