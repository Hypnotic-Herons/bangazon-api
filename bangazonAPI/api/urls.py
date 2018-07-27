from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import customer, training_view

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', customer.CustomerViewSet)
router.register('training', training_view.TrainingView)


urlpatterns = [
    path('', include(router.urls))
]

