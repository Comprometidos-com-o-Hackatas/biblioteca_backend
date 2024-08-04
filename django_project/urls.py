"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.biblioteca.views import CategoriaViewSet, GeneroViewSet, AutoresViewSet, LivroViewSet, LivroPegoViewSet
from core.usuario.router import router as usuarioRouter
from core.uploader.router import router as uploaderRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r'generos', GeneroViewSet, basename='generos')
router.register(r'autores', AutoresViewSet, basename='autores')
router.register(r'categorias', CategoriaViewSet)
router.register(r'livro', LivroViewSet)
router.register(r'livropego', LivroPegoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(usuarioRouter.urls)),
    path('api/media/', include(uploaderRouter.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name="swagger"),
    path('api/redoc/', SpectacularRedocView.as_view(), name="redoc"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)