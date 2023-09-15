from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from apps.ecommerce.models import Venta
from apps.ecommerce.serializers.venta_serializers import VentaSerializer
from apps.ecommerce.models.producto import Prodcuto


class VentaViewSet(GenericViewSet):

    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def list(self, request):
        """
        Endpoint: Listado de ventas realizadas
        ---
        Body: N/A
        ---
        Response:
        [
            {
                "id": str,
                "producto_nombre": str,
                "producto_descripcion": str,
                "cantidad_vendida": int,
                "producto_precio": decimal,
                "fecha": datetime
            },
            ...
        ]
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Endpoint para efectuar una venta.
        ---
        Body:
        {
            "producto": id_producto,
            "cantidad_vendida": int
        }
        ---
        Response:
        {
            "id": str,
            "producto": {
                ...datos del producto
            },
            "cantidad_vendida": int,
            "fecha": datetime
        }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto_id = serializer.validated_data["producto"].id
        producto = Prodcuto.objects.get(id=producto_id)
        producto.cantidad_disponible -= serializer.validated_data["cantidad_vendida"]
        producto.save()

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def ventas_totales(self, request):
        """
        Endpoint: Número total de ventas realizadas
        ---
        Body: N/A
        ---
        Response:
        {
            "ventas_totales": int
        }
        """
        total_ventas = self.get_queryset().count()
        return Response({"ventas_totales": total_ventas})
