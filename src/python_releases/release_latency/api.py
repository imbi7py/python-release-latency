from rest_framework import viewsets

from .models import PythonImplementation, PythonRelease
from .serializers import PythonImplementationSerializer, PythonReleaseSerializer


class PythonImplementationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Python implementations to be viewed & updated.
    """
    queryset = PythonImplementation.objects.all()
    serializer_class = PythonImplementationSerializer


class PythonReleaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PythonRelease.objects.all().order_by('-release_date')
    serializer_class = PythonReleaseSerializer