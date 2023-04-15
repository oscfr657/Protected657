from django.urls import path, re_path, include

from protected657.views import ProtectedFileCreate, ProtectedFileList, ProtectedFileView

from .routers import PROTCTEDFILES_ROUTER

app_name = 'protected657'
urlpatterns = [
    path('', ProtectedFileList.as_view(), name='list'),
    path('add/', ProtectedFileCreate.as_view(), name='add'),
    path(
        'media/<path:relative_path>',
        ProtectedFileView.as_view(),
        name='protected-media'),
    re_path(r'^api/', include(PROTCTEDFILES_ROUTER.urls), name='api'),
]
