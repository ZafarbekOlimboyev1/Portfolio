from django_filters import FilterSet, CharFilter, NumberFilter
from django.db.models import Q

from uzbek_poets_app.models import PoemsModel, PoetsModel


class PoetsFilter(FilterSet):
    search = CharFilter(method='my_filter', label='Search')

    class Meta:
        model = PoetsModel
        fields = []

    def my_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(poet_name__icontains=value) |
                Q(poet_description__icontains=value) |
                Q(poet_about__icontains=value) |
                Q(poet_birthdate__icontains=value) |
                Q(poet_dead_date__icontains=value))
        else:
            return queryset


class PoemsFilter(FilterSet):
    search = CharFilter(method='my_filter', label='Search')

    class Meta:
        model = PoemsModel
        fields = []
    
    def my_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(poem_name__icontains=value) |
                Q(poem_poem__icontains=value) |
                Q(poem_poet_id__poet_name__icontains=value),
                Q(poem_poet_id__poet_description__icontains=value),
                Q(poem_poet_id__poet_about__icontains=value),
                Q(poem_poet_id__poet_birthdate__icontains=value),
                Q(poem_poet_id__poet_dead_date__icontains=value),
            )
        return queryset