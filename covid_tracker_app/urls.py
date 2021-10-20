from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:userid>/', views.user, name='user'),
    path('register/', views.register_user, name='register')
]