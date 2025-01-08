from django.urls import path
from . import views

app_name= 'job'
urlpatterns = [
    path('', views.Job_type),
    path('<int:id>', views.Job_details, name='job'),
]