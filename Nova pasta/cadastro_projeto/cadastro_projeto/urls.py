from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro_app.urls')),  # Inclui todas as URLs do cadastro_app
]
