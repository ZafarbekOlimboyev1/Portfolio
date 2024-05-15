from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RegisterView, reset_password, UserView, ChangePasswordView

router = DefaultRouter()
router.register('update', UserView, basename='update')

urlpatterns = [
    path('update/password/', ChangePasswordView.as_view()),
    path('reset/', reset_password),
    path('', RegisterView.as_view()),
] + router.urls
