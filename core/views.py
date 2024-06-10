from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from . models import Books


# Create your views here.
def api_view(request, pk):
    all_books = Books.objects.get(pk=pk)
    return JsonResponse(model_to_dict(all_books))