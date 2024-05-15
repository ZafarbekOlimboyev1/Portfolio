from rest_framework.serializers import ModelSerializer, CharField, CurrentUserDefault

from .models import NewsModel, AnnouncementsModel, LeadershipModel, StructuralUnitsModel


class NewsSerializer(ModelSerializer):
    author = CharField(default=CurrentUserDefault())

    class Meta:
        model = NewsModel
        fields = '__all__'


class AnnouncementsSerializer(ModelSerializer):
    author = CharField(default=CurrentUserDefault())

    class Meta:
        model = AnnouncementsModel
        fields = '__all__'


class LeadershipSerializer(ModelSerializer):
    author = CharField(default=CurrentUserDefault())

    class Meta:
        model = LeadershipModel
        fields = '__all__'


class StructuralUnitsSerializer(ModelSerializer):
    author = CharField(default=CurrentUserDefault())

    class Meta:
        model = StructuralUnitsModel
        fields = '__all__'
