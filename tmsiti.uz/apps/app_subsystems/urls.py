from rest_framework.routers import DefaultRouter

from .views import (GroupsViewSet, DocumentsViewSet,
                    DocPartsViewSet, SubsystemsViewSet,
                    DocPlanViewSet, DocTypesViewSet,
                    DocSubPlanViewSet, DictionaryViewSet)


router = DefaultRouter()

router.register('subsystems', SubsystemsViewSet, basename='Subsystems')
router.register('groups', GroupsViewSet, basename='Groups')
router.register('documents', DocumentsViewSet, basename='Documents')
router.register('documents-parts', DocPartsViewSet, basename="Document Parts")
router.register('documents-plans', DocPlanViewSet, basename='Document Plans')
router.register('documents-subplans', DocSubPlanViewSet, 'Document Subplans')
router.register('documents-parts', DocTypesViewSet, 'Document Types')
router.register('dictionary', DictionaryViewSet, 'Dictionary')

urlpatterns = router.urls
