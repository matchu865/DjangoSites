from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$(?P<course_id>[0-9]+)/', views.course, name = 'course'),
	url(r'^$', views.index, name = 'index'),


]