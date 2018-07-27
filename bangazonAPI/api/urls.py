
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

router.register(r'training', views.TrainingView)


urlpatterns = [
    url(r'^', include(router.urls))
]