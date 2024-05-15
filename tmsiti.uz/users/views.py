import random
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from users.models import PasswordResetModel, CustomUser
from users.serializers import UserCreateSerializer, UserSerializer, ChangePasswordSerializer
from .permissions import Cheak


class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(["GET", "POST"])
def reset_password(request):
    if request.method == 'GET':
        user = CustomUser.objects.filter(username=request.data.get('email')).first()
        if user:
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)
            code = PasswordResetModel.objects.create(user_id=user, reset_code=f'{num1}{num2}')
            code.save()
            send_mail(
                subject="Reset Password",
                message=f"Your confirm code {num1}-{num2}",
                from_email="forlesson02@gmail.com",
                recipient_list=[request.data.get('email')],
                fail_silently=False,
            )
            return Response(data={"status": "success", "code": status.HTTP_200_OK,
                                  "message": "Code sent successfully."
                                             "The code is valid for 10 minutes",
                                  "email": request.data.get('email')})
        else:
            return Response(data={"status": "filed", "code": status.HTTP_404_NOT_FOUND,
                                  "message": "Email not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        code = request.data.get('code')
        new_password = request.data.get('new_password')
        if code is None or new_password is None:
            return Response(
                data={
                    'status': 'failed',
                    'reuired fileds': {
                        'code': int,
                        'new_password': str
                    }
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            reset_user = PasswordResetModel.objects.filter(reset_code=code, is_valid=True).last()
            if reset_user is None:
                return Response(
                    data={
                        'status': 'failed',
                        'message': 'invalid code'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                user = CustomUser.objects.filter(pk=reset_user.user_id)
                user.set_password(new_password)
                user.save()
                return Response(
                    data={
                        'status': 'success',
                        'message': 'Password successfully changed'
                    },
                    status=status.HTTP_200_OK
                )
    else:
        return Response(
            data={
                'status': 'fail',
                'message': 'This method is not allowed'
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class UserView(ModelViewSet):
    queryset = get_user_model()
    serializer_class = UserSerializer
    http_method_names = ('get', 'put', 'patch')
    permission_classes = [Cheak, ]


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



