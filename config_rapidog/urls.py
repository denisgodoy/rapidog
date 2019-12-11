"""config_rapidog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rapidog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('produtos/', views.produtos),
    path('produtos/alimentacao/', views.alimentacao),
    path('produtos/higiene/', views.higiene),
    path('produtos/brinquedos/', views.brinquedos),
    path('petshops/', views.lojas),
    path('produtos/<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('perfil/', views.perfil),
    path('contato/', views.contato),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
