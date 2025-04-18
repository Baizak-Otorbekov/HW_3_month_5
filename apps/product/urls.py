from django.urls import path
from apps.product.views import ProductListCreateAPIView

urlpatterns = [
    path('product_list/', ProductListCreateAPIView.as_view(), name='list')
]
