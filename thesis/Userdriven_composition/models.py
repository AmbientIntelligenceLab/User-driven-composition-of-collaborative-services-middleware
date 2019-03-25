from django.db import models
from datetime import datetime

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