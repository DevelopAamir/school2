from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('404', views.notfound, name='404'),
    path('students', views.students, name='students'),
    path('staff', views.staff, name='staff'),
    path('parents', views.parents, name='parents'),
    path('register/<str:type>/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('sections/<int:grade>/', views.sections, name='sections'),
]