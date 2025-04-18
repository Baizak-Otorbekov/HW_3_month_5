from rest_framework.generics import ListCreateAPIView
from apps.  product.models import Product, ProductImage
from apps.product.serializer import ProductSerializer, ProductImageSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer