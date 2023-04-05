from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about/",views.about,name='About'),
    path("caesarcipher/",views.caesarcipher,name='caesarcipher'),
]
