from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    # Lectura pública, escritura solo con Token
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
