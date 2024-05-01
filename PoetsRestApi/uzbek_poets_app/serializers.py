from rest_framework import serializers

from uzbek_poets_app.models import PoetsModel, PoemsModel


class UzbekPoetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoetsModel
        fields = ['id', 'poet_name', 'poet_description', 'poet_image']
        ordering = ('poet_name', )


class UzbekPoetsAllInfoSerializer(serializers.ModelSerializer):
    poet_user_id = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoetsModel
        fields = '__all__'


class UzbekPoemsSerializer(serializers.ModelSerializer):
    poem_poet_details = serializers.SerializerMethodField('get_poem_poet_details')
    poem_user_id = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoemsModel
        fields = [
            'id', 'poem_name', 'poem_poem',
            'poem_poet_id', 'poem_poet_details',
            'poem_user_id', 'poem_written_time']

    def get_poem_poet_details(self, object):
        details = {
            'poet_id': object.poem_poet_id.pk,
            'poet_name': object.poem_poet_id.poet_name,
            'poet_description': object.poem_poet_id.poet_description,
            'poet_details': f'http:127.0.0.1:8000/api/v1/poets/{object.poem_poet_id.pk}'
        }
        return details
