
from django.contrib import admin
from django.urls import path
from main.views import cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/',cadastro, name='cadastro')
]
