from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page=''), name="logout"),
    path('cadastrar-aniversariante',
         views.register_birthday, name='register_birthday'),
    path('cadastrar-usuario', views.register_user, name='register_user'),
    path('configuracao', views.profile, name='profile')
]
