from django.db import models

# Create your models here.
class Actuator(models.Model):
	status = models.IntegerField()
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class LowerSensor(models.Model):
	value = models.IntegerField()
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name