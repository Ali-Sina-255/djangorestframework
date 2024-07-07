from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import StudentModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentListApiView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['name', 'score']
    ordering_fields = ['name', 'score']
    search_fields = ['^id', 'name']
    ordering = ['score']


@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "GET":
        student = StudentModel.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    # return Response


@api_view(["GET", "PUT", "DELETE"])
def student_detail_view(request, pk):
    try:
        student = StudentModel.objects.get(pk=pk)
    except StudentModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
