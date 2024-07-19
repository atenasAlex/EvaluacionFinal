from django.contrib import admin
from .models import Producto
# Register your models here.

admin.site.register(Producto)

admin.site.site_header = 'Administración Ferremas'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Ferremas'