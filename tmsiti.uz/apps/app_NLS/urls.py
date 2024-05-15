from rest_framework.routers import DefaultRouter

from .views import AnnouncementsViewSet, LeadershipViewSet, NewsViewSet, StructuralUnitsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'announcements', AnnouncementsViewSet, basename='announcements')
router.register(r'leadership', LeadershipViewSet, basename='leadership')
router.register('StructuralUnits', StructuralUnitsViewSet, basename='StructuralUnits')

urlpatterns = router.urls
