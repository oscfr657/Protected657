from rest_framework import serializers

from .models import ProtectedFile


class ProtectedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectedFile
        fields = ('pk', 'title', 'file', 'created_by', 'site')
