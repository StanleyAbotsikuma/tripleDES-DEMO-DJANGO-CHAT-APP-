from django.urls import path
from .views import single_page,single_page1
urlpatterns = [
    path("",single_page),
    path("mobile/",single_page1)
]