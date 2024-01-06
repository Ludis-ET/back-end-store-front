from django.urls import path
from .views import *
from rest_framework_nested import routers 

router = routers.DefaultRouter()
router.register('products',ProductViewSet)
router.register('collections',CollectionViewSet)

products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',ReviewViewSet,basename='product-reviews')
 
urlpatterns = router.urls + products_router.urls
