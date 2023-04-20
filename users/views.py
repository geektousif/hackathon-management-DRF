
from django.contrib.auth import login, logout, authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        if email is None or password is None:
            return Response({'error': 'Enter email/password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:

            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logout Success'}, status=status.HTTP_200_OK)
