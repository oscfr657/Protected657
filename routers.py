from rest_framework import routers

from .views import ProtectedFileViewSet


PROTCTEDFILES_ROUTER = routers.DefaultRouter()
PROTCTEDFILES_ROUTER.register(r'protected_files', ProtectedFileViewSet)