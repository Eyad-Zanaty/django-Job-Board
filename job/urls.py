from django.urls import path
from . import views

app_name= 'job'
urlpatterns = [
    path('', views.Job_type),
    path('<str:slug>', views.Job_details, name='job'),
]