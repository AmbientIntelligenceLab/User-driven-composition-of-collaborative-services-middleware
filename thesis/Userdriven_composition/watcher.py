from .models import Service_registry

class Watcher(object):

    def __init__(self):
        pass

    def watch(self):
        service_registry = Service_registry.objects.latest('id')
        return service_registry