from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('activate/<str:uidb64>/<str:token>/',
         views.activate_account, name="activate"),
    path('login/', views.login_view, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',
         views.password_reset_confirm, name='password_reset_confirm'),
]
