from django_filters.filterset import FilterSet, CharFilter
from django.db.models import Q

from .models import ElectronicStandardsModel


class ElectronicStandardsFilter(FilterSet):
    search = CharFilter(method='search_filter', label="Search")
    category = CharFilter(method='category_filter', label='Category')
    conditional_sign = CharFilter(method='conditional_sign_filter', label='ConditionalSign')
    year = CharFilter(method='year_filter', label='Year')

    class Meta:
        model = ElectronicStandardsModel
        fields = []

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(standard_type__electronic_standard_type__icontains=value) |
            Q(standard_code__icontains=value) |
            Q(standard_description__icontains=value) |
            Q(standard_text__icontains=value)
        )

    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(standard_type__electronic_standard_type__icontains=value))

    def conditional_sign_filter(self, queryset, name, value):
        return queryset.filter(Q(standard_code__icontains=value))

    def year_filter(self, queryset, name, value):
        try:
            return queryset.filter(Q(year=int(value)))
        except:
            return None


