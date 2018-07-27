from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.product_type import ProductTypeView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product_type', ProductTypeView)

urlpatterns = [
   path('', include(router.urls))
]