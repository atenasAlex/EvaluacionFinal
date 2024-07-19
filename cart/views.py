from django.shortcuts import render, get_object_or_404
from .cart import Cart
from api.models import Producto
from django.http import JsonResponse
from .mercado import preference
from django.shortcuts import render, redirect
from pages.views import obtener_valor_dolar

# Create your views here.

from django.shortcuts import render


def pago(request):

    valor_dolar = obtener_valor_dolar()
    cart = Cart(request)
    envio_precio = 5000
    totals = cart.cart_total()

    if request.method == 'POST':
        nombre = request.POST.get('txtName', '')  
        direccion = request.POST.get('txtDirecc', '')  
        numero = request.POST.get('numDirec', '')  
        comuna = request.POST.get('txtComuna', '') 
        region = request.POST.get('sRegion', '')
        totalenvio = float(totals)
        envio = envio_precio

        
        context = {
            'nombre': nombre,
            'direccion': direccion,
            'numero': numero,
            'comuna': comuna,
            'region':region,
            'totalenvio': totalenvio,
            'envio': envio,
            'valor_dolar': valor_dolar,

        }
        
        return render(request, "pago.html",context)

        


def cart_summary(request):
    valor_dolar = obtener_valor_dolar()
    envio_precio = 5000
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    envio = envio_precio

    return render(request,"cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "envio":envio, 'valor_dolar': valor_dolar,})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        producto_codigo = int(request.POST.get('producto_codigo'))
        producto_qty = int(request.POST.get('producto_qty'))
        producto = get_object_or_404(Producto, codigo = producto_codigo)
        
        cart.add(producto=producto, quantity=producto_qty)

        cart_quantity = cart.__len__()


        #response = JsonResponse({'Nombre del producto: ': producto.nombre})
        response = JsonResponse({'qty': cart_quantity})
        return response




def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        producto_codigo = int(request.POST.get('producto_codigo'))

        cart.delete(producto=producto_codigo)

        response = JsonResponse({'producto': producto_codigo})
        return response



def cart_update(request):
    pass

