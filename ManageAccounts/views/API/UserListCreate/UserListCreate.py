# List all users and create a new user
from rest_framework import generics

from ManageAccounts.models import CustomUser
from ManageAccounts.serializers import CustomUserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        serializer.save()
