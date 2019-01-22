from rest_framework import serializers
from .models import *

class ActuatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actuator
		fields = ('topic','value', 'time', 'name')

class LowerSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actuator
		fields = ('topic','value', 'time', 'name')
