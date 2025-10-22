"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.index),
    path('add_student/',views.add_student),
    path('add_course/',views.add_course),
    path('report_student/',views.report),
    path('movies/',views.movie_list, name='movie_list'),
    path('movies/<int:pk>/',views.movie_detail, name='movie_detail'),
    path('movies/add/',views.add_movie, name='add_movie'),
    path('movies/<int:pk>/edit/',views.edit_movie, name='edit_movie'),
    path('movies/<int:pk>/delete/',views.delete_movie, name='delete_movie'),
]
