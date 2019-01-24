from . import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('actuators', views.ActuatorApi)
router.register('lowersensors', views.LowerSensorApi)

urlpatterns = [
    # url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$',views.notice_detail, name ='notice_detail')
    path('',views.home, name = 'home_url'),
    path('api/',include(router.urls)),
    path('getMotorStatus/',views.getMotorStatus, name='status'),
]
