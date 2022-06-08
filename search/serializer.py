from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        if obj.id == 20:
            return "Modified from serializer"
        return "Not id 20"

    class Meta:
        model = Product
        fields = '__all__'
