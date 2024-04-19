
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bookstore/', include('bookstore_app.urls')),
    path('admin/', admin.site.urls),
]
