from .models import Service_registry
from django.db.models import signals


def service_added(sender,instance,created, **kwargs):
	print('new service added')

signals.post_save.connect(receiver=service_added,sender=Service_registry)