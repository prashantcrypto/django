from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [


    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('project/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),


]
