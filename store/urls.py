from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('products',ProductViewSet)
router.register('collections',CollectionViewSet)
urlpatterns = router.urls
