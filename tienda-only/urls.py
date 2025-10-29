from django.contrib import admin
from django.urls import path, include
from shop import views


urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", include("shop.urls")),
    path("admin/", admin.site.urls),
]
