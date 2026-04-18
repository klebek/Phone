from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("Hello from Django on the phone!")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
