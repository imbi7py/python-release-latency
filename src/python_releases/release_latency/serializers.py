from rest_framework import serializers

from .models import PythonImplementation, PythonRelease

class PythonImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PythonImplementation
        fields = ('url', 'name')


class PythonReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PythonRelease
        fields = ('url', 'implementation', 'version', 'release_date', 'kind')
