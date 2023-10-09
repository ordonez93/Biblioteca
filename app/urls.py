#importar urls
from django.urls import path,include

from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'libros', views.LibroViewSet, 'libros')
router.register(r'autores', views.AutorViewSet, 'autores')
router.register(r'categorias', views.CategoriaViewSet, 'categorias')
router.register(r'prestamos', views.PrestamosViewSet, 'prestamos')
router.register(r'personas', views.PersonaViewSet, 'personas')
router.register(r'libro_categoria', views.LibroCategoriaViewSet, 'libro_categoria')
router.register(r'libro_autor', views.LibroAutorViewSet, 'libro_autor')
router.register(r'usuario_persona', views.UsuarioPersonaViewSet, 'usuario_persona')
urlpatterns = [
    path('api/', include(router.urls))
    
]