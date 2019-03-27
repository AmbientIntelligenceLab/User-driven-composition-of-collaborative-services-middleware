from django.contrib import admin
from .models import Actuator,LowerSensor,Service_registry
# Register your models here.
admin.site.register(Actuator)
admin.site.register(LowerSensor)
admin.site.register(Service_registry)

