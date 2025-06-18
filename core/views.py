from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView

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
