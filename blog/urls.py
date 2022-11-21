from django.urls import path
from blog import views

urlpatterns = [


    path('', views.blog, name='blog'),
    path('<str:slug>', views.component, name='component'),
    


]
