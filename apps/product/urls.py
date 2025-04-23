from rest_framework.routers import DefaultRouter
from apps.product.views import ProductMixins

router = DefaultRouter()
router.register(r'products', ProductMixins, basename='products')

urlpatterns = router.urls