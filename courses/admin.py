from django.contrib import admin
from . models import Course, Assignment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'description', 'starting_time')


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'description', 'deadline')


admin.site.register(Assignment, AssignmentAdmin)

admin.site.register(Course, CourseAdmin)

