from . import views
from django.urls import path

urlpatterns = [
    # url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$',views.notice_detail, name ='notice_detail')
    path('',views.home, name = 'home_url'),
]