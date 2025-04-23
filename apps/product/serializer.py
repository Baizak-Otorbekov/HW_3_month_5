from rest_framework import serializers
from apps.product.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ('image', 'position')

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'is_active', 'product_images', 'created_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        product_images_data = self.context['request'].FILES.getlist('product_images')
        product = Product.objects.create(**validated_data)

        for idx, image in enumerate(product_images_data):
            ProductImage.objects.create(product=product, image=image, position=idx)
        
        return product