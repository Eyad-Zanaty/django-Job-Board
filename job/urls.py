from django.urls import path
from . import views

urlpatterns = [
    path('', views.Job_type),
    path('<int: id>', views.Job_details),
]