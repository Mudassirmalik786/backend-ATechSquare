from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            res = Response({"success": True})
            res.set_cookie("access", str(refresh.access_token), httponly=True)
            res.set_cookie("refresh", str(refresh), httponly=True)
            return res
        return Response({"error": "Invalid Credentials"}, status=400)
    
class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("id_token")
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), "your-google-client-id.apps.googleusercontent.com")
            email = idinfo["email"]
            name = idinfo.get("name", "")
            user, created = User.objects.get_or_create(email=email, defaults={"username": email.split('@')[0]})
            refresh = RefreshToken.for_user(user)
            res = Response({'success': True})
            res.set_cookie('access', str(refresh.access_token), httponly=True)
            res.set_cookie('refresh', str(refresh), httponly=True)
            return res
        except Exception as e:
            return Response({'error': 'Invalid Google token'}, status=400)
