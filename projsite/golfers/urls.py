from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<course_id>[0-9]+)/', views.course, name = 'course'),

	url(r'^adduser/', views.adduser, name = 'adduser'),
	url(r'^addcourse/', views.addcourse, name = 'addcourse'),

	url(r'^$', views.index, name = 'index'),
]