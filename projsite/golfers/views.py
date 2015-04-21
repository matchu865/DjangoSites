from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Golfer, Round,Course

def index(request):
	golfer_list = Golfer.objects.order_by('-last_name')
	round_list = Round.objects.order_by('-golfer')
	course_list = Course.objects.order_by('-course_name')

	context = {'golfer_list' : golfer_list, 'round_list' : round_list, 'course_list' : course_list}

	return render(request, 'golfers/index.html', context)


def submitted(request):
	return HttpResponse("Thanks for submitting")

def course(request, course_id):
	
	course = Course.objects.get(pk = course_id)
	return HttpResponse("in course view" + course_id)	