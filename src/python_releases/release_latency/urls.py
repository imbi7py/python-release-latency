from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import api

router = routers.DefaultRouter()
router.register(r'implementations', api.PythonImplementationViewSet)
router.register(r'releases', api.PythonReleaseViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
