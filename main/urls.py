from django import urls
from django.urls import include, path

from main import views


urlpatterns = [
    path("products-t/", views.ProductAPIView.as_view()),
]

