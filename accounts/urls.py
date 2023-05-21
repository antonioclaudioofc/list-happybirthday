from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastra-se', views.register, name='register'),
    path('configuracao', views.profile, name='profile')
]