from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user_model.models import User
from user_model.serializers import UserSerializer
from .authentication import SafeJWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class VerifyTokenView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    def post(self, request):
        if request.user:
            account = request.user
            user = User.objects.get(account__username=account.username)
            return JsonResponse({"user_id": user.id, "message": "Token is valid"}, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)

class UserInfoView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        account = request.user  # Lấy user hiện tại từ request

        try:
            user_instance = User.objects.get(account__username=account.username)
            serializer = UserSerializer(user_instance)

            user_data = {
                'id': serializer.data['id'],
                'username': serializer.data['account']['username'],
                'email': serializer.data['email'],
                'first_name': serializer.data['fullname']['first_name'],
                'last_name': serializer.data['fullname']['last_name'],
                'full_name': f"{serializer.data['fullname']['first_name']} {serializer.data['fullname']['last_name']}",
                'phone': serializer.data['phone'],
                'address': serializer.data['address']['address']
            }

            return Response(user_data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
