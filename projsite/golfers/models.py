import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Golfer(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = 	models.CharField(max_length = 30)
	age = 		models.IntegerField(default = 30, validators = [MinValueValidator(1),])

	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Course(models.Model):
	course_name = 	models.CharField(max_length = 60)
	par = 			models.IntegerField(default = 72)
	city = 			models.CharField(max_length = 30)
	state = 		models.CharField(max_length = 2)

	def __unicode__(self):
		return self.course_name

	
class Round(models.Model):
	golfer = 	models.ForeignKey('Golfer')
	course = 	models.ForeignKey('Course')
	round_date= models.DateTimeField('date published')
	score = 	models.IntegerField(default = 72, validators = [MinValueValidator(50),])
	gir = 		models.IntegerField(default = 12, validators = [MinValueValidator(0), MaxValueValidator(18)])
	putts = 	models.IntegerField(default = 36, validators = [MinValueValidator(0),])
	fairways = 	models.IntegerField(default = 12, validators = [MinValueValidator(0), MaxValueValidator(18)])

	def __unicode__(self):
		return unicode(self.golfer) + " " + \
			unicode(self.course)  + " " + \
			self.round_date.strftime('%x ') +  "" + \
			unicode(self.score)




