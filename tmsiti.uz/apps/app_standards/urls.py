from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    StandardsViewSet, StandardTypesViewSet,
    ElectronicStandardsViewSet, ElectronicStandardTypesViewSet,
    BuildingRegulationsViewSet, MessagesView)

router = DefaultRouter()
router.register('Standards', StandardsViewSet, basename='Standards')
router.register('Electronic-Standards', ElectronicStandardsViewSet, basename='Electronic Standards')
router.register('Building-Regulations', BuildingRegulationsViewSet, basename='Building Regulations')
router.register('Standard-Types', StandardTypesViewSet, basename='Standard Types')
router.register('Electronic-StandardTypes', ElectronicStandardTypesViewSet, basename='Electronic Standard Types')

urlpatterns = [
    path('send-message/', MessagesView.as_view())
] + router.urls
