from django.urls import path
from .views import single_page
urlpatterns = [
    path("",single_page),
]