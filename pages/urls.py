from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tienda/", views.tienda, name="tienda"),
    path("compra/<str:codigo>/", views.compra, name="compra"),
    path("servicio-al-cliente/", views.customer_service, name="customer_service"),
    path('customer-service/success/', views.customer_service_success, name='customer_service_success'),

]
