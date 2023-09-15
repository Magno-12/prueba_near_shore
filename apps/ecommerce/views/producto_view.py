from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.ecommerce.models.producto import Prodcuto
from apps.ecommerce.serializers.producto_serializer import ProductoSerializer


class ProdcutoViewSet(GenericViewSet):

    queryset = Prodcuto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request):
        """
        Endpoint: Listado de productos
        ---
        Body: N/A
        ---
        Response:
        {
            "id": str,
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int
            "fecha": datetime
        }
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Endpoint: Crear un nuevo producto
        ---
        Body:
        {
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int
        }
        ---
        Response:
        {
            "id": str,
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int
            "fecha": datetime
        }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        """
        Endpoint: Actualizar detalles de un producto
        ---
        Body:
        {
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int
        }
        ---
        Response:
        {
            "id": str,
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int
            "fecha": datetime
        }
        """
        predio = self.get_object()
        serializer = self.get_serializer(predio, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Endpoint: Obtener detalles de un producto
        ---
        Body: N/A
        ---
        Response:
        {
            "id": str,
            "nombre": str,
            "descripcion": str,
            "precio": decimal,
            "cantidad_disponible": int,
            "fecha": datetime
        }
        """
        producto = self.get_object()
        serializer = self.get_serializer(producto)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Endpoint: Eliminar un producto
        ---
        Body: N/A
        ---
        Response:
        {
            "message": "Producto eliminado con éxito."
        }
        """
        producto = self.get_object()
        producto.delete()
        return Response({"message": "Producto eliminado con éxito."},
            status=status.HTTP_200_OK
        )
