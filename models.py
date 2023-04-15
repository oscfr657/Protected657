import magic

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.sites.models import Site
from django.core.files.storage import FileSystemStorage


protected_storage = FileSystemStorage(
    location='protected/files/',
    base_url='/protected/media/',
)


class ProtectedFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(storage=protected_storage)
    file_type = models.CharField(max_length=25, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True)
    # password = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return u'%s' % self.file.name

    def __str__(self):
        if self.title:
            return u'%s' % self.title
        return u'%s' % self.file.name

    def save(self, *args, **kwargs):
        # First doing a normal save
        super(ProtectedFile, self).save()
        # Then we try to get the file_type
        try:
            file_type = magic.from_buffer(self.file.file.read(), mime=True)
            self.file_type = file_type
            super(ProtectedFile, self).save()
        except (IOError, ValueError, AttributeError):
            pass  # We should probably handle and or log this.
