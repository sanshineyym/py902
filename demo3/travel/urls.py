from django.conf.urls import url
from . import views
app_name='travel'
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact')
]