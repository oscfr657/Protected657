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
    
    def remove_on_file_update(self):
        try:
            # is the object in the database yet?
            obj = ProtectedFile.objects.get(id=self.id)
        except ProtectedFile.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual file?
        if obj.file and self.file and obj.file != self.file:
            # delete the old file from the storage in favor of the new file
            obj.file.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.file.delete()
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_file_update()
        # First doing a normal save
        super().save(*args, **kwargs)
        # Then we try to get the file_type
        try:
            file_type = magic.from_buffer(self.file.file.read(), mime=True)
            self.file_type = file_type
            super().save()
        except (IOError, ValueError, AttributeError):
            pass  # We should probably handle and or log this.
