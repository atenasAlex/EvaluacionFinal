from django.views import View
from .models import Producto
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, codigo=0, marca=""):
        if (codigo > 0):
            productos=list(Producto.objects.filter(codigo=codigo).values())
            if len(productos) > 0:
                producto=productos[0]
                datos={'message': "Success", 'producto':producto}

            else:
                datos={'message': "Producto no encontrado"}
            return JsonResponse(datos)
        
        
        elif marca:
            productos = list(Producto.objects.filter(marca=marca).values())
            if productos:
                datos = {'message': "Success", 'productos': productos}
            else:
                datos = {'message': "Productos no encontrados para la marca especificada"}
            return JsonResponse(datos)



        else:
            productos=list(Producto.objects.values())
            if len(productos)>0:
                datos={'message': "Success", 'productos':productos}
            else:
                datos={'message': "Productos no encontrado"}
            return JsonResponse(datos)


    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Producto.objects.create(codigo=jd['codigo'], marca=jd['marca'], nombre=jd['nombre'], precio=jd['precio'])
        datos={'message': "Success"}
        return JsonResponse(datos)
    

    def put(self, request, codigo):
        jd=json.loads(request.body)
        productos=list(Producto.objects.filter(codigo=codigo).values())
        if len(productos) > 0:
            producto=Producto.objects.get(codigo=codigo)
            producto.codigo=jd['codigo']
            producto.marca=jd['marca']
            producto.nombre=jd['nombre']
            producto.precio=jd['precio']
            producto.save()
            datos={'message': "Success"}
        else:
            datos={'message': "Producto no encontrado"}
        return JsonResponse(datos)
            


    def delete(self, request, codigo):
        productos=list(Producto.objects.filter(codigo=codigo).values())
        if len(productos) > 0:
            Producto.objects.filter(codigo=codigo).delete()
            datos={'message': "Success"}
        else:
            datos={'message': "Producto no encontrado"}
        return JsonResponse(datos)

        
