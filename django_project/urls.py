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
from core.biblioteca.views import CategoriaViewSet, GeneroViewSet, AutoresViewSet, LivroViewSet, LivroPegoViewSet, AvaliacaoViewSet, FavoritoViewSet, BlockedBooksViewSet
from core.usuario.views import UsuarioViewSet
from core.biblioteca.views import CategoriaViewSet, GeneratePDFView, GeneroViewSet, AutoresViewSet, LivroViewSet, LivroPegoViewSet, FamiliaViewSet
from core.usuario.router import router as usuarioRouter
from core.uploader.router import router as uploaderRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r'generos', GeneroViewSet, basename='generos')
router.register(r'autores', AutoresViewSet, basename='autores')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'avaliacao', AvaliacaoViewSet, basename='avaliacoes')
router.register(r'favorito', FavoritoViewSet, basename='favorito')
router.register(r'livro', LivroViewSet)
router.register(r'livropego', LivroPegoViewSet, basename='livros_pegos')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'blocked_books', BlockedBooksViewSet, basename='blocked_books')
router.register(r'familias', FamiliaViewSet, basename='familias')

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include(usuarioRouter.urls)),
    path('api/media/', include(uploaderRouter.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name="swagger"),
    path('api/redoc/', SpectacularRedocView.as_view(), name="redoc"),
    path('generate-pdf/', GeneratePDFView.as_view(), name='generate_pdf'),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)