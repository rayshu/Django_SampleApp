from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:userid>/', views.user, name='user'),
]