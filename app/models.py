from django.db import models
from django.contrib.auth.models import auth, User

# Create your models here.

class Persona(models.Model):
    identificacion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre + " " + self.apellido

class Autor(models.Model):
    nombre_autor= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_autor

class categoria(models.Model):
    nombre_categoria= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_categoria

class libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    editorial = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo
    
class libro_categoria(models.Model):
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.libro + " " + self.categoria

class libro_autor(models.Model):
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.libro + " " + self.autor
    
class prestamos(models.Model):
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_prestamo = models.CharField(max_length=50)
    fecha_devolucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    def __str__(self):
        return self.libro + " " + self.user

class usuario_persona(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return self.user + " " + self.persona
    
