from django.urls import path
from pageHome.views import home

urlpatterns = [
    path('',home),
]