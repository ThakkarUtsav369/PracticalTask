from rest_framework.routers import DefaultRouter

from .views import UploadCsvViewSet
from django.urls import path, include

router=DefaultRouter()

router.register('uploadCsv',UploadCsvViewSet,basename='uploadcsv')

urlpatterns = [
    path("", include(router.urls)),
]