"""vapormap URL Configuration

"""
import os
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views as apiviews
from django.conf.urls.static import static
from vapormap import settings

router = routers.DefaultRouter()
router.register(r'points', apiviews.PointViewSet, 'points')

# r'^$' point to SinglePageApp in front package
# r'^api/' is manage by DjangoRestFramework to manage
# r'^/geojson$' is a special endpoint to retrieve data as GeoJSON
# static contents from front should be expose as /static
urlpatterns = [
    path('api/', include(router.urls)),
    path('geojson', apiviews.GeoJson.as_view(), name="geojson")
]
# Si mode developpement, on demande au serveur de developpement de présenter les /static
# Sinon, c'est le serveur http qui le fera
if os.environ['DJANGO_SETTINGS_MODULE'] == 'vapormap.settings.development':
    urlpatterns += static(settings.development.STATIC_URL,
                          document_root=settings.development.STATIC_ROOT)

