from django.urls import include, path
from rest_framework import routers

from hospitals.router import HospitalViewSet

router = routers.DefaultRouter()
router.register('', HospitalViewSet)

app_name = 'hospitals'
urlpatterns = [
    path('', include(router.urls)),
]
