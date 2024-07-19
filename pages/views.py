from django.shortcuts import render, redirect
import folium.map
from api.models import Producto
from django.conf import settings
from django.core.mail import EmailMessage
import folium
from django.contrib.auth.decorators import login_required
from .models import Location
import requests

# Create your views here.

import requests
from django.conf import settings

def obtener_valor_dolar():
    url = "https://cl.dolarapi.com/v1/cotizaciones/usd"
    try:
        response = requests.get(url, timeout=5)  
        response.raise_for_status()  
        data = response.json()
        valor_dolar = data.get("ultimoCierre")  
        if valor_dolar is None:
            return None  
        return valor_dolar
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el valor del dólar: {e}")
        return None

def home(request):    
    valor_dolar = obtener_valor_dolar()
    locations = Location.objects.all()
    initialMap = folium.Map(location=[-33.43292210194037, -70.61491263182941], zoom_start=18)
    for location in locations:
        coordinates = (location.lat, location.lng)
        folium.Marker(coordinates, popup='Sucursal' + location.name).add_to(initialMap)
    map_html = initialMap._repr_html_()
    productosListado = Producto.objects.all()
    

    context = {

        'map': map_html, 
        'locations':locations,
        'valor_dolar': valor_dolar,

        }
    
    return render(request, "index.html", context)



def tienda(request):

    dolar_context = obtener_valor_dolar()
    marca = request.GET.get("marca")
    if marca:
        productosListado = Producto.objects.filter(marca__icontains=marca)
    else:
        productosListado = Producto.objects.all()


    return render(request, "tienda.html", {"productos": productosListado})


def compra(request, codigo):
    productoSpecific = Producto.objects.get(codigo=codigo)
    return render(request, "compra.html", {"producto": productoSpecific})

def customer_service_success(request):
    return render(request, "customer_service_success.html")

def customer_service(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        full_message = (
            f"Nombre: {name}\nCorreo Electrónico: {email}\n\nMensaje:\n{message}"
        )

        email_message = EmailMessage(
            subject="Consulta de Servicio al Cliente",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=["jul.contreraso@duocuc.cl"],
        )
        email_message.content_subtype = "plain"
        email_message.encoding = "utf-8"

        email_message.send(fail_silently=False)

        return redirect("customer_service_success")

    return render(request, "customer_service.html")





