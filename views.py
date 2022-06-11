import mimetypes
from urllib.parse import quote

from django.conf import settings
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import  HttpResponse, HttpResponseForbidden
from django.urls import reverse
from django.views.static import serve
from django.views import View

from .models import ProtectedFile


class ProtectedFileList(LoginRequiredMixin, ListView):
    model = ProtectedFile
    def get_queryset(self):
        queryset = ProtectedFile.objects.all()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                created_by=self.request.user
            )
        return queryset


class ProtectedFileCreate(LoginRequiredMixin, CreateView):
    model = ProtectedFile
    fields = ['title', 'file']

    def get_success_url(self):
        return reverse('protected657:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProtectedFileView(View):
    def get(self, request, relative_path):
        protected_file = get_object_or_404(ProtectedFile, file=relative_path)
        if not (request.user.is_superuser or protected_file.created_by == request.user):
            return HttpResponseForbidden()
        if settings.DEBUG:
            response = serve(
                request, protected_file.file.name, document_root=settings.PROTECTED_MEDIA_ROOT,
                show_indexes=False
            )
        else:
            response = HttpResponse()
            response['Content-Type'] = mimetypes.guess_type(protected_file.file.name)[0]
            response['Content-Disposition'] = f'attachment; filename={protected_file.file.name}'
            url_path = quote(f'/internal/{protected_file.file.name}')
            response['X-Accel-Redirect'] = url_path
        return response
