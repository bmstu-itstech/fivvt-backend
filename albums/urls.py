from django.urls import include, path
from rest_framework import routers

from albums.router import AlbumViewSet


router = routers.DefaultRouter()
router.register('', AlbumViewSet)

app_name = 'albums'
urlpatterns = [
    path('', include(router.urls)),
]
