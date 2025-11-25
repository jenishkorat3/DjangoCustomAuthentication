from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('customer/', include('customer.urls')),
    path('seller/', include('seller.urls')),
    path('product/', include('product.urls')),
]
