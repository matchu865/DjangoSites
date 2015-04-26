from django import forms
from django.forms import ModelForm
from .models import Course, Golfer, Round
from datetime import date

class NameForm(forms.Form):
	your_name = forms.CharField(label = 'Your name', max_length=100)


class GolferModelForm(forms.ModelForm):
	class Meta:
		model = Golfer
		fields ='__all__'

#we might only allow the admin to add courses
class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['course_name', 'par', 'city', 'state',]

class RoundModelForm(forms.ModelForm):
	class Meta:
		model = Round
		round_date = forms.DateField(label = 'date published', input_formats = ['%Y-%m-%d %H:%M'], initial=date.today)
		fields = '__all__'
