from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PoetsViewSet, PoemsViewSet

router = DefaultRouter()


router.register(r'poets', PoetsViewSet, basename="name1")
router.register(r'poems', PoemsViewSet, basename="name2")

urlpatterns = router.urls
