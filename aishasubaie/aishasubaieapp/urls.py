# filepath: /Users/aishakhaled/Desktop/Experiment1/djangolab1/aishasubaie/aishasubaieapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
]