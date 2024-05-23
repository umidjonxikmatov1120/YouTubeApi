from django.contrib.auth import authenticate
from django.shortcuts import render
from django_filters import filters, Filter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from videos.models import Videos
from videos.serializers import VideoSerializer


class VideoViewset(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        title = self.request.query_params.get('query', None)

        if title is not None:
            queryset = queryset.filter(title=title)

        return queryset


class TokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

