from rest_framework.serializers import ModelSerializer

from .models import (DocumentPartsModel, DocumentPlanModel,
                     DocumentsModel, DocumentTypesModel,
                     GroupsModel, DocumentSubPlansModel,
                     SubsystemsModel, DictionaryModel)


class SubsystemsSerializer(ModelSerializer):
    class Meta:
        model = SubsystemsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = GroupsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = DocumentsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DocumentTypesSerializer(ModelSerializer):
    class Meta:
        model = DocumentTypesModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DocumentPartsSerializer(ModelSerializer):
    class Meta:
        model = DocumentPartsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DocumentPlanSerializer(ModelSerializer):
    class Meta:
        model = DocumentPlanModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DocumentSubPlansSerializer(ModelSerializer):
    class Meta:
        model = DocumentSubPlansModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class DictionarySerializer(ModelSerializer):

    class Meta:
        model = DictionaryModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }
