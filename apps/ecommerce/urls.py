from django.urls import include, path

from rest_framework import routers

from apps.ecommerce.views.producto_view import ProdcutoViewSet
from apps.ecommerce.views.venta_view import VentaViewSet

router = routers.DefaultRouter()

router.register(r'producto', ProdcutoViewSet, basename='producto')
router.register(r'venta', VentaViewSet, basename='venta')

urlpatterns = [
    path('', include(router.urls)),
]
