from django.contrib import admin

from .models import Golfer, Round, Course

admin.site.register(Golfer)
admin.site.register(Round)
admin.site.register(Course)
