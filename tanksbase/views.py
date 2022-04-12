from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from tanksbase.models import Tank
from tanksbase.serializers import TankSerializer


def heroku_view(request):
    return render(request, 'field_modernization_heroku.html')


def local_view(request):
    return render(request, 'field_modernization.html')


class TankView(ModelViewSet):
    queryset = Tank.objects.order_by('-tier', 'type')
    serializer_class = TankSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'tier', 'nation', 'type']
    search_fields = ['name']
    ordering_fields = ['tier', 'nation', 'type']
    permission_classes = [IsAuthenticatedOrReadOnly]
