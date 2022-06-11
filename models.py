
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


protected_storage = FileSystemStorage(
    location='protected/files/',
    base_url='/protected/media/',
    )


class ProtectedFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(storage=protected_storage)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
