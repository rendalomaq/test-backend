from django import urls
from django.urls import include, path

from main import views


urlpatterns = [
    path("products/", views.ProductAPIView.as_view()),
]

"""
urlpatterns = [
    path("products/", include("domains.rest.suppliers.v100.urls")),
]
"""
