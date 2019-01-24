from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
def home(request):
	return render(request, 'index.html')

def getMotorStatus(request):
    #csrfContext = RequestContext(code)
    if request.is_ajax():
        code = request.POST['code']
        #function_call = request.POST['function_call']
        #motor_status = get_action_motor_status(function_call)
        print(code)
        exec(code)
    else:
        return HttpResponse('Use ajax format!')

    return JsonResponse({'code': code })


def get_lowersensor():
    return 130

def action_motor(status):
    pass


class ActuatorApi(viewsets.ModelViewSet):
	queryset = Actuator.objects.all()
	serializer_class = ActuatorSerializer

class LowerSensorApi(viewsets.ModelViewSet):
	queryset = LowerSensor.objects.all()
	serializer_class = LowerSensorSerializer
