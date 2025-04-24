from rest_framework import serializers
from apps.product.models import Product, ProductImage, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ('image', 'position')

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=False, required=False)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'is_active', 
                 'product_images', 'created_at', 'category', 'category_id')
        read_only_fields = ('id', 'created_at', 'category')

    def create(self, validated_data):
        product_images_data = self.context['request'].FILES.getlist('product_images')
        category = validated_data.pop('category', None)
        
        product = Product.objects.create(**validated_data)
        if category:
            product.category = category
            product.save()

        for idx, image in enumerate(product_images_data):
            ProductImage.objects.create(product=product, image=image, position=idx)
        
        return product