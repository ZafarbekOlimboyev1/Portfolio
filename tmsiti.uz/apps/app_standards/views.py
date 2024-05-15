from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination


from .permissions import Cheak
from .models import (StandardTypesModel, StandardsModel,
                     ElectronicStandardsModel, ElectronicStandardTypesModel,
                     BuildingRegulationsModel, MessagesModel)

from .serializers import (StandardsSerializer, StandardTypesSerializer,
                          ElectronicStandardsSerializer, ElectronicStandardsGetSerializer,
                          ElectronicStandardTypesSerializer, BuildingRegulationsSerializer,
                          BuildingRegulationsGetSerializer, MessagesSerializer)

from .filters import ElectronicStandardsFilter


class StandardTypesViewSet(ModelViewSet):
    queryset = StandardTypesModel.objects.all()
    serializer_class = StandardTypesSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['StandardTypes'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StandardTypes'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['StandardTypes'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['StandardTypes'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StandardTypes'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['StandardTypes'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StandardsViewSet(ModelViewSet):
    queryset = StandardsModel.objects.all()
    serializer_class = StandardsSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['Standards'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Standards'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Standards'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Standards'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Standards'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Standards'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ElectronicStandardsViewSet(ModelViewSet):
    queryset = ElectronicStandardsModel.objects.all()
    permission_classes = [Cheak, ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ElectronicStandardsFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "GET" and 'pk' not in self.kwargs:
            return ElectronicStandardsGetSerializer
        else:
            return ElectronicStandardsSerializer

    @swagger_auto_schema(tags=['Electronic Standards'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standards'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standards'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standards'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standards'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standards'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ElectronicStandardTypesViewSet(ModelViewSet):
    queryset = ElectronicStandardTypesModel.objects.all()
    serializer_class = ElectronicStandardTypesSerializer
    permission_classes = [Cheak, ]

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Electronic Standard Types'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BuildingRegulationsViewSet(ModelViewSet):
    queryset = BuildingRegulationsModel.objects.all()
    permission_classes = [Cheak, ]

    def get_serializer_class(self):
        if self.request.method == "GET" and 'pk' not in self.kwargs:
            return BuildingRegulationsGetSerializer
        else:
            return BuildingRegulationsSerializer

    @swagger_auto_schema(tags=['Building Regulations'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Building Regulations'])
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Building Regulations'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(tags=['Building Regulations'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Building Regulations'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Building Regulations'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessagesView(CreateAPIView):
    model = MessagesModel
    serializer_class = MessagesSerializer

    @swagger_auto_schema(tags=['Messages'])
    def post(self, request, *args, **kwargs):
        data = request.data
        msg = (f"FullName: {data.get('msg_fio')}\n"
               f"Phone number: {data.get('msg_phone_number')}\n"
               f"Email: {data.get('msg_email')}\n"
               f"LeaderShip: {data.get('msg_management')}\n"
               f"\nMessage:\n\t {data.get('msg_text')}")
        send_mail(
            subject="You have a new message!",
            message=msg,
            from_email="forlesson02@gmail.com",
            recipient_list=['zafarbekolimboyev07@gmail.com'],  # admin email
            fail_silently=False,
        )
        return super().post(self, request, *args, **kwargs)

