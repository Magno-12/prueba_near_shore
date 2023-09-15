from rest_framework import serializers

from apps.ecommerce.models.producto import Prodcuto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodcuto
        fields = '__all__'

    def validate_precio(self, value):
        """
        Comprueba que el precio es mayor que 50.
        """
        if value <= 50:
            raise serializers.ValidationError("El precio debe ser mayor que 50.")
        return value
