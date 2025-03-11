from django.urls import include, path
from rest_framework import routers

from board.router import BoardViewSet

router = routers.DefaultRouter()
router.register('', BoardViewSet)

app_name = 'board'
urlpatterns = [
    path('', include(router.urls)),
]
