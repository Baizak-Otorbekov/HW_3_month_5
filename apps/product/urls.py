from rest_framework.routers import DefaultRouter
from apps.product.views import ProductMixins, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductMixins, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls