from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns = [
    path('Signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('Profile/edit', views.profile_edit, name='profile_edit'),
]