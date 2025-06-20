
from django.contrib import admin
from django.urls import path, include
from final_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("user.urls")),
    path("", main, name="main"),
    path("vacancy/", include("vacancy.urls")),
    path("info/", info, name="info")
]
