from django.urls import path, include 

from . import views 

app_name = "app_new"

urlpatterns = [
    path('', views.index, name="main"), 
]

