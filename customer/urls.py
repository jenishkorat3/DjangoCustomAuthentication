from django.urls import path
from . import views

urlpatterns = [
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('change_password/', views.change_password, name='change_password'),
]
