from django.db import models
from datetime import datetime
from django.db.models import signals
import requests
from . import automatic_writter


def service_added(sender,instance,created, **kwargs):
	# service = Service_registry.objects.last()
	# last_service_datas = requests.get("http://127.0.0.1:8000/api/serviceregistry/{}/".format(service.id)).json()
	# #used for data logging
	print('new service added!')
	# last_service_id = last_service_datas['id']
	# last_service_name = last_service_datas['name']
	# #edit name_id
	# last_service_name_id = last_service_datas['name_id']
	# last_service_api_link = last_service_datas['api_link']
	# last_service_service_type = last_service_datas['service_type']
	# #checking purpose
	# if last_service_service_type == 'sensor':
	# 	automatic_writter.sensor_function_writter(last_service_name_id,last_service_api_link)
	# elif last_service_service_type == 'actuator':
	# 	automatic_writter.actuator_function_writter(last_service_name_id,last_service_api_link)
	#val(service.id,service.name,service.name_id,service.api_link,service.service_type)
	#print('{} {}'.format(service.id, service.name))

#for initializing 
def val(id,name,name_id,api_link,service_type):
	id = id
	name = name
	name_id = name_id
	api_link = api_link
	service_type = service_type

# Create your models here.
class Actuator(models.Model):
	topic = models.CharField(max_length=100, null = True)
	value = models.CharField(max_length=100, null = True)
	time = models.DateTimeField(auto_now_add=True,null = True)
	name = models.CharField(max_length=60, null = True)

	def __str__(self):
		return self.name


class LowerSensor(models.Model):
	topic = models.CharField(max_length=100, null = True)
	value = models.CharField(max_length=100, null = True)
	time = models.DateTimeField(default=datetime.now, null=True)
	name = models.CharField(max_length=60, null = True)

	def __str__(self):
		return self.name


class Service_registry(models.Model):
	name = models.CharField(max_length=50)
	name_id = models.CharField(max_length=100)
	api_link = models.CharField(max_length=200)
	service_type = models.CharField(max_length=50)

	def __str__(self):
		return self.name



signals.post_save.connect(receiver=service_added,sender=Service_registry)