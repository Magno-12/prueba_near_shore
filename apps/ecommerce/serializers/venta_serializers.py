from rest_framework import serializers

from apps.ecommerce.models import Venta
from apps.ecommerce.models.producto import Prodcuto

class VentaSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Prodcuto.objects.all())
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_descripcion = serializers.CharField(source='producto.descripcion',
        read_only=True
    )
    producto_precio = serializers.DecimalField(source='producto.precio',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )
    
    class Meta:
        model = Venta
        fields = [
            'id',
            'producto',
            'producto_nombre',
            'producto_descripcion',
            'cantidad_vendida',
            'producto_precio',
            'fecha'
        ]

    def validate(self, data):
        """
        Comprueba que la cantidad vendida es menor o igual a la cantidad disponible en el stock.
        """
        cantidad_vendida = data.get('cantidad_vendida')
        producto = data.get('producto')

        if isinstance(producto, (int, str)):
            producto = Prodcuto.objects.get(pk=producto)
        """
        Ahora, obtenemos la cantidad disponible del producto
        """
        if producto:
            cantidad_disponible = producto.cantidad_disponible
            if cantidad_vendida > cantidad_disponible:
                raise serializers.ValidationError({
                    "cantidad_vendida": 
                    f"La cantidad vendida ({cantidad_vendida}) no puede ser mayor que la cantidad disponible ({cantidad_disponible})."
                })

        return data
