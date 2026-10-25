from django.contrib import admin
from django.urls import path
from site import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("site/", views.home, name="home"),
]
