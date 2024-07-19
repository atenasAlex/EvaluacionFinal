from django.urls import path
from .views import ProductoView

urlpatterns =[
    path('productos/', ProductoView.as_view(), name='productos_list'),
    path('productos/<int:codigo>', ProductoView.as_view(), name='productos_process'),
    path('productos/<str:marca>', ProductoView.as_view(), name='productos_marca')
]