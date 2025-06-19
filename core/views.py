from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .validators import SignupSerializer, LoginSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)

            res = Response({"success": True})
            res.set_cookie("access", str(refresh.access_token), httponly=True)
            res.set_cookie("refresh", str(refresh), httponly=True)
            return res

        return Response(serializer.errors, status=400)


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = User.objects.create_user(username=username, email=email, password=password)

            refresh = RefreshToken.for_user(user)
            res = Response({"success": True})
            res.set_cookie("access", str(refresh.access_token), httponly=True)
            res.set_cookie("refresh", str(refresh), httponly=True)
            return res

        return Response(serializer.errors, status=400)
