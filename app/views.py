# vistas basadasa en los serializadores
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = libro.objects.all()
    serializer_class = LibroSerializer

class LibroAutorViewSet(viewsets.ModelViewSet):
    queryset = libro_autor.objects.all()
    serializer_class = LibroAutorSerializer

class LibroCategoriaViewSet(viewsets.ModelViewSet):
    queryset = libro_categoria.objects.all()
    serializer_class = LibroCategoriaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = prestamos.objects.all()
    serializer_class = PrestamosSerializer

class UsuarioPersonaViewSet(viewsets.ModelViewSet):
    queryset = usuario_persona.objects.all()
    serializer_class = UsuarioPersonaSerializer

