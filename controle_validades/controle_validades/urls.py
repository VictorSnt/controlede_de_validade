from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('expiration_control/', include('expiration_control.urls')),
    path('admin/', admin.site.urls),
]
