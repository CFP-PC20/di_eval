from django.contrib import admin
from .models import Articulo

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    pass

admin.site.register(Articulo,ArticuloAdmin)