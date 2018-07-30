
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'training', views.TrainingView)
router.register(r'customers', views.CustomerViewSet)
router.register(r'product_type', views.ProductTypeViewSet)
router.register(r'computer', views.ComputerViewSet)

router.register(r'department', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]