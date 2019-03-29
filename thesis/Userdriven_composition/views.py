from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def home(request):
	return render(request, 'index.html')


class ActuatorApi(viewsets.ModelViewSet):
	queryset = Actuator.objects.all()
	serializer_class = ActuatorSerializer

class LowerSensorApi(viewsets.ModelViewSet):
	queryset = LowerSensor.objects.all()
	serializer_class = LowerSensorSerializer


class ServiceRegistryApi(viewsets.ModelViewSet):
	queryset = Service_registry.objects.all()
	serializer_class = ServiceRegistrySerializer
