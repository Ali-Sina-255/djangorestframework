from django.urls import path
from . import views
urlpatterns = [
    path('book/<int:pk>/', views.api_view, name='index'),
]
