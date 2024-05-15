from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField

from .models import (
    StandardTypesModel, StandardsModel,
    ElectronicStandardTypesModel, ElectronicStandardsModel,
    BuildingRegulationsModel, MessagesModel
)


class StandardTypesSerializer(ModelSerializer):

    class Meta:
        model = StandardTypesModel
        fields = '__all__'


class StandardsSerializer(ModelSerializer):

    class Meta:
        model = StandardsModel
        fields = '__all__'


class ElectronicStandardsSerializer(ModelSerializer):

    class Meta:
        model = ElectronicStandardsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True},
        }


class ElectronicStandardsGetSerializer(ModelSerializer):

    class Meta:
        model = ElectronicStandardsModel
        fields = [
            'standard_type', 'standard_code',
            'standard_description', 'is_active'
        ]


class ElectronicStandardTypesSerializer(ModelSerializer):

    class Meta:
        model = ElectronicStandardTypesModel
        fields = '__all__'


class BuildingRegulationsSerializer(ModelSerializer):

    class Meta:
        model = BuildingRegulationsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class BuildingRegulationsGetSerializer(ModelSerializer):

    class Meta:
        model = BuildingRegulationsModel
        fields = ['doc_number', 'doc_type', 'doc_code', 'doc_title']


class MessagesSerializer(Serializer):

    class Meta:
        model = MessagesModel
        fields = ['msg_fio']
