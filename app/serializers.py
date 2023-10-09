#serializar los modelos
from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro
        fields = '__all__'

class LibroAutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro_autor
        fields = '__all__'

class LibroCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro_categoria
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = prestamos
        fields = '__all__'

class UsuarioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_persona
        fields = '__all__'


