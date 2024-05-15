from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import pretty_name

from .serializers import (GroupsSerializer, DocumentsSerializer,
                          DocumentSubPlansSerializer, SubsystemsSerializer,
                          DocumentPartsSerializer, DocumentPlanSerializer,
                          DocumentTypesSerializer, DictionarySerializer)

from .models import (SubsystemsModel, GroupsModel,
                     DocumentPlanModel, DocumentsModel,
                     DocumentPartsModel, DocumentTypesModel,
                     DocumentSubPlansModel, DictionaryModel)

from .permissions import Cheak


class SubsystemsViewSet(ModelViewSet):
    queryset = SubsystemsModel.objects.all()
    serializer_class = SubsystemsSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Subsystems'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Subsystems'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Subsystems'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Subsystems'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Subsystems'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Subsystems'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(ModelViewSet):
    queryset = GroupsModel.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Groups'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Groups'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Groups'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Groups'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Groups'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Groups'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DocTypesViewSet(ModelViewSet):
    queryset = DocumentTypesModel.objects.all()
    serializer_class = DocumentTypesSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Documents'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Documents'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Documents'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Documents'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Documents'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Documents'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DocumentsViewSet(ModelViewSet):
    queryset = DocumentsModel.objects.all()
    serializer_class = DocumentsSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Document Parts'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Parts'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Parts'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Parts'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Parts'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Parts'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DocPartsViewSet(ModelViewSet):
    queryset = DocumentPartsModel.objects.all()
    serializer_class = DocumentPartsSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Document Plans'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Plans'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Plans'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Plans'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Plans'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Plans'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DocPlanViewSet(ModelViewSet):
    queryset = DocumentPlanModel.objects.all()
    serializer_class = DocumentPlanSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Document Subplans'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Subplans'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Subplans'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Subplans'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Subplans'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Subplans'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DocSubPlanViewSet(ModelViewSet):
    queryset = DocumentSubPlansModel.objects.all()
    serializer_class = DocumentSubPlansSerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(tags=['Document Types'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Types'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Types'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Types'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Types'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Document Types'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DictionaryViewSet(ModelViewSet):
    queryset = DictionaryModel.objects.all()
    pretty_name('Dictionary')
    serializer_class = DictionarySerializer
    permission_classes = [Cheak, ]
    pagination_class = PageNumberPagination

    # @swagger_auto_schema(tags=['Dictionary'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Dictionary'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Dictionary'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Dictionary'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Dictionary'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Dictionary'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
