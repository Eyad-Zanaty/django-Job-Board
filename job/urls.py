from django.urls import path
from . import views

app_name= 'job'
urlpatterns = [
    path('', views.Job_type, name='job_list'),
    path('Apply', views.apply_job, name='apply_job'),
    path('<str:slug>', views.Job_details, name='job'),
]