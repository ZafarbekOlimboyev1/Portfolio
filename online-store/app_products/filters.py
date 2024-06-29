from django_filters.filterset import FilterSet, CharFilter
from django.db.models import Q

from .models import ProductsModel


class ProductsFilterSet(FilterSet):
    search = CharFilter(method='get_search', label='Search')

    class Meta:
        model = ProductsModel
        fields = []

    def get_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(utils__icontains=value) |
            Q(description__icontains=value) | Q(category_id__category__icontains=value)
        )

