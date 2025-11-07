from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('', views.predict_flower, name='predict_flower'),
]
