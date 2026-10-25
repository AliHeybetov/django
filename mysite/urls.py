from django.contrib import admin
from django.urls import path
from wikipedia import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wikipedia/", views.home, name="home"),
]
