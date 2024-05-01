from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission

from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import PoemsFilter, PoetsFilter
from .models import PoetsModel, PoemsModel
from .serializers import UzbekPoemsSerializer, UzbekPoetsAllInfoSerializer, UzbekPoetsSerializer


# My permissions
class Cheak_poet(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        elif request.method == "POST":
            return request.user.is_confirmed
        return request.user == view.get_object().poet_user_id or request.user.is_superuser


class Cheak_poem(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        elif request.method == "POST":
            return request.user.is_confirmed
        return request.user == view.get_object().poem_user_id or request.user.is_superuser


# work with Poets
class PoetsViewSet(ModelViewSet):
    queryset = PoetsModel.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [Cheak_poet, ]
    filterset_class = PoetsFilter
    authentication_classes = [JWTAuthentication, ]

    def get_serializer_class(self):
        if self.request.method == 'GET' and 'pk' not in self.kwargs:
            return UzbekPoetsSerializer
        return UzbekPoetsAllInfoSerializer


# work with Poems
class PoemsViewSet(ModelViewSet):
    queryset = PoemsModel.objects.all()
    serializer_class = UzbekPoemsSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [Cheak_poem, ]
    filterset_class = PoemsFilter
    authentication_classes = [JWTAuthentication, ]
