# Retrieve, update, or delete a user
from rest_framework import generics

from ManageAccounts.models import CustomUser
from ManageAccounts.serializers import CustomUserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

