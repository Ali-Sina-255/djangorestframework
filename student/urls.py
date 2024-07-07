from django.urls import path
from . import views

urlpatterns = [
    path("", views.StudentListApiView.as_view(), name="student-list"),
    path("<int:pk>/", views.student_detail_view, name="student-detail"),
]
