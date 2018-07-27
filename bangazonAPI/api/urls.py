from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]