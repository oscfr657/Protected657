from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site
from .models import ProtectedFile


class ProtectedFileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(
            created_by=request.user,
            site=get_current_site(self.request))

admin.site.register(ProtectedFile, ProtectedFileAdmin)
