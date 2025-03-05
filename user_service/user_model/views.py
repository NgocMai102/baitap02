from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from user_model.models import User
from user_model.serializers import UserSerializer
from rest_framework import status

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            user['account']['password'] = ''  # Xóa password trước khi trả về response
            return Response({'status': 'success', "user": user}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
