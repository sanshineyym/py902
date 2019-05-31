from django.conf.urls import url

from car import views
app_name='car'

urlpatterns =[
    url(r'^index/$', views.index, name='index'),
    url(r'single/$', views.single, name='single'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^other/$',views.other,name='other')


]