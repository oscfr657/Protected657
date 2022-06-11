try:
    from django.urls import path
except ImportError:
    from django.conf.urls import path

from protected657.views import ProtectedFileCreate, ProtectedFileList, ProtectedFileView


app_name = 'protected657'
urlpatterns = [
    path('', ProtectedFileList.as_view(), name='list'),
    path('add/', ProtectedFileCreate.as_view(), name='add'),
    path('media/<path:relative_path>', ProtectedFileView.as_view(), name='protected-media'),
]
