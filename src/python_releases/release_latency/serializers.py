from rest_framework import serializers

from .models import PythonImplementation, PythonRelease

class PythonImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PythonImplementation
        fields = ('url', 'name')

class _RelatedNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class PythonReleaseSerializer(serializers.HyperlinkedModelSerializer):
    implementation = _RelatedNameField(read_only=True)

    class Meta:
        model = PythonRelease
        fields = ('url', 'implementation', 'version', 'release_date', 'kind')
