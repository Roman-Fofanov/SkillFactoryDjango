from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import BaseRegisterView, login_view, login_with_code_view


urlpatterns = [
    path('login/',
         login_view,
         name='login'),
    path('code/',
         login_with_code_view,
         name='code_login'),
    path('logout/',
         LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='account/signup.html'),
         name='signup'),
]