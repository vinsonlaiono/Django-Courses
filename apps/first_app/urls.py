from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^process', views.process),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^remove/(?P<id>\d)$', views.remove),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^delete/(?P<id>\d)$', views.delete),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    
   # This line has changed! Notice that urlpatterns is a list, the comma is in
                                # url(r'^test', views.test),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                   
