from django.urls import path, include

from .views import RegisterView, ChangePasswordView, ConfirmEmailView, send_code

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('update/password/', ChangePasswordView.as_view()),
    path('send-code-email/', send_code),
    path('confirm-email/', ConfirmEmailView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
