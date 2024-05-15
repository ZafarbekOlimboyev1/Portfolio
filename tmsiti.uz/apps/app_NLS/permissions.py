from rest_framework.permissions import BasePermission


class Cheak(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user == view.get_object().author or request.user.is_superuser
