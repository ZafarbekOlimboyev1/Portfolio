import random
from django.conf import settings

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from users.serializers import UserSerializer, ChangePasswordSerializer, ConfirmEmailSerializer
from .sended_codes import codes


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmailView(UpdateAPIView):
    serializer_class = ConfirmEmailSerializer
    model = get_user_model()

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        code = request.data
        print(code, str(codes[request.user.username]))
        if code.get('sent_code') == str(codes[request.user.username]):
            self.object.is_confirmed = True
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Email confirmed successfully',
                'data': []
            }

            return Response(response)

        return Response({'Code invalid. Please try again'})


@api_view(['GET'])
def send_code(request):
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    codes[request.user.username] = f"{num1}{num2}"
    print(codes[request.user.username])
    send_mail(
        subject="Confirm Email",
        message=f"Your confirm code {num1}{num2}",
        from_email="forlesson02@gmail.com",
        recipient_list=[request.user.email],
        fail_silently=False,
    )
    return Response({"status": "success", "code": status.HTTP_200_OK, "message": "Code sent successfully", "data": [],
                     "email": request.user.email})
