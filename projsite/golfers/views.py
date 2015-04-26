from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse

from .forms import NameForm,GolferModelForm,CourseModelForm,RoundModelForm, CourseSelectForm

from .models import Golfer, Round,Course

def index(request):
	golfer_list = Golfer.objects.order_by('-last_name')
	round_list = Round.objects.order_by('-score').reverse()
	course_list = Course.objects.order_by('-course_name')

	#handle adding round
	if request.method == 'POST':
		roundModelForm = RoundModelForm(request.POST)		
		if roundModelForm.is_valid():
			#need to redirect to their course page
			roundModelForm.save()
			courseid = roundModelForm.cleaned_data['course'].id
			return HttpResponseRedirect(reverse('golfers:course', args=(courseid,)))
		
		courseSelectForm = CourseSelectForm(request.POST)
		if courseSelectForm.is_valid():
			courseid = courseSelectForm.cleaned_data['course'].id
			return HttpResponseRedirect(reverse('golfers:course', args=(courseid,)))

	else:
		roundModelForm = RoundModelForm()
	context = {'golfer_list' : golfer_list, 
				'round_list' : round_list, 
				'course_list' : course_list,
				'roundModelForm' : roundModelForm,
				'courseSelectForm' : CourseSelectForm}
	
	return render(request, 'golfers/index.html', context)

#Very similiar to index but takes a course_id argument
def course(request, course_id):
	golfer_list = Golfer.objects.order_by('-last_name')
	localcourse = Course.objects.filter(pk = course_id)
	round_list = Round.objects.filter(course = localcourse)
	round_list = round_list.order_by('-score').reverse()

	if request.method == 'POST':
		roundModelForm = RoundModelForm(request.POST)
		if roundModelForm.is_valid():
			#need to redirect to their course page
			roundModelForm.save()
			courseid = roundModelForm.cleaned_data['course'].id
			return HttpResponseRedirect(reverse('golfers:course', args=(courseid,)))
		
		courseSelectForm = CourseSelectForm(request.POST)
		if courseSelectForm.is_valid():
			courseid = courseSelectForm.cleaned_data['course'].id
			return HttpResponseRedirect(reverse('golfers:course', args=(courseid,)))
	else:
		roundModelForm = RoundModelForm()

	context = {'round_list' : round_list,
				'golfer_list' : golfer_list,
				'course_list' : localcourse,
				'roundModelForm' : roundModelForm,
				'courseSelectForm': CourseSelectForm}
	# return HttpResponse("HI: " + str(round_list[0]))
	return 	render(request, 'golfers/index.html', context)


def adduser(request):
	if request.method == 'POST':
		golferModelForm = GolferModelForm(request.POST)
		if golferModelForm.is_valid():
			golferModelForm.save()

			return HttpResponseRedirect(reverse('golfers:index'))
	else:
		golferModelForm = GolferModelForm()
	return render(request, 'golfers/form.html', {'golferModelForm' : golferModelForm})

def addcourse(request):
	if request.method == 'POST':
		courseModelForm = CourseModelForm(request.POST)
		if courseModelForm.is_valid():
			courseModelForm.save()
			name = courseModelForm.cleaned_data['course_name']
			course = Course.objects.get(course_name = name)
			return HttpResponseRedirect(reverse('golfers:course', args = (course.id,)))
	else:
		courseModelForm = CourseModelForm()
	return render(request, 'golfers/form.html', {'courseModelForm' : courseModelForm})






def create(request):
	if request.method == 'POST':
		courseModelForm = CourseModelForm(request.POST)
		golferModelForm = GolferModelForm(request.POST)
		roundModelForm = RoundModelForm(request.POST)
		if roundModelForm.is_valid() and golferModelForm.is_valid() and roundModelForm.is_valid():
			return HttpResponse('Thanks')
	else:
		roundModelForm = RoundModelForm()
		golferModelForm = GolferModelForm()
		courseModelForm = CourseModelForm()
	return render(request, 'golfers/create.html', {'roundModelForm': roundModelForm,
				 'courseModelForm': courseModelForm, 'golferModelForm' : golferModelForm})

##attempting to inline forms on the first try :/
# def create(request):
# 	GolferInlineFormSet = inlineformset_factory(Golfer, Round, form = GolferModelForm)

# 	if request.method == 'POST':
# 		roundModelForm = RoundModelForm(request.POST)

# 		if roundModelForm.is_valid():
# 			new_round = roundModelForm.save()
# 			golferInlineFormSet = GolferInlineFormSet(request.POST, request.FILES, instance = new_round)

# 			if GolferInlineFormSet.is_valid():
# 				golferInlineFormSet.save()
# 				## need to figure out where I'm sending them but for now
# 				return HttpResponse("Thanks for submitting!!")
# 			else:
# 				classificationformset = ClassificationInlineFormSet(request.POST, request.FILES, instance=new_round)

# 	else:
# 		golferInlineFormSet = GolferInlineFormSet()
# 		roundModelForm = RoundModelForm()
# 	return render(request, 'golfers/create.html', {'roundModelForm': roundModelForm})


