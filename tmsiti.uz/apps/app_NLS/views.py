from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from .serializers import NewsSerializer, AnnouncementsSerializer, LeadershipSerializer, StructuralUnitsSerializer
from .models import LeadershipModel, AnnouncementsModel, NewsModel, StructuralUnitsModel
from .permissions import Cheak


class NewsViewSet(ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['News'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['News'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['News'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['News'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['News'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['News'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnnouncementsViewSet(ModelViewSet):
    queryset = AnnouncementsModel.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['Announcements'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Announcements'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Announcements'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Announcements'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Announcements'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Announcements'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LeadershipViewSet(ModelViewSet):
    queryset = LeadershipModel.objects.all()
    serializer_class = LeadershipSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['Leadership'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Leadership'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Leadership'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Leadership'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Leadership'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Leadership'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StructuralUnitsViewSet(ModelViewSet):
    queryset = StructuralUnitsModel.objects.all()
    serializer_class = StructuralUnitsSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['StructuralUnits'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StructuralUnits'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['StructuralUnits'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['StructuralUnits'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StructuralUnits'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StructuralUnits'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
