from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls")),
    path("", include("student.urls")),
    path("api/", include("snapp.urls")),
    path("flight/", include("flightApp.urls")),
]
