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


#service registry serializer
class ServiceRegistrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Service_registry
		fields = ('id','name','name_id','api_link','service_type')
