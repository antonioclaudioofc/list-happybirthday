from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    # path('sair', LogoutView.as_view(next_page='login.html'), name="logout"),
    path('cadastra-se', views.register, name='register'),
    path('configuracao', views.profile, name='profile')
]
