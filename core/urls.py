from django.urls import path, include
from . import views as v
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produto', v.ProdutoViewSet)
router.register('compra', v.CompraViewSet)
router.register('compraproduto', v.CompraProdutoViewSet)
router.register('user', v.UserViewSet)


urlpatterns = router.urls