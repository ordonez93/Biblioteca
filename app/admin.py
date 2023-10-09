from django.contrib import admin

# Register your models here.
from .models import Autor, categoria, libro, libro_autor, libro_categoria, Persona, prestamos, usuario_persona

admin.site.register(Autor)
admin.site.register(categoria)
admin.site.register(libro)
admin.site.register(libro_autor)
admin.site.register(libro_categoria)
admin.site.register(Persona)
admin.site.register(prestamos)
admin.site.register(usuario_persona)

