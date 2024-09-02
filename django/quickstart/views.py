from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class FetchDataFromFastAPI(APIView):
    def get(self, request, *args, **kwargs):
        fastapi_url = "http://localhost:8990/items/1"  # Replace with your FastAPI service URL
        response = requests.get(fastapi_url)
        
        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response({"error": "Failed to retrieve data from FastAPI"}, status=response.status_code)
