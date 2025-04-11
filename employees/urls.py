from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, RoleViewSet, ContactInfoViewSet, EmployeeRoleHistoryViewSet, employee_tree_view

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'contact-info', ContactInfoViewSet)
router.register(r'role-history', EmployeeRoleHistoryViewSet)

urlpatterns = [
    path('employees/tree/', employee_tree_view, name='employee-tree'),
    path('', include(router.urls)),
]
