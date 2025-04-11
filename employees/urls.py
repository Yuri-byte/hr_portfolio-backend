from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, RoleViewSet, ContactInfoViewSet, EmployeeRoleHistoryViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'contact-info', ContactInfoViewSet)
router.register(r'role-history', EmployeeRoleHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
