from rest_framework.views import APIView, status, Response
from rest_framework.generics import ListCreateAPIView
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import pdb

class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

