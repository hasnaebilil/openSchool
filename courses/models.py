from django.db import models
import datetime
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField()
    description = models.CharField(max_length=2083)
    video_url = models.CharField(max_length=2083)
    starting_time = timezone.now()


class Assignment(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    deadline = timezone.now() + datetime.timedelta(days=30)
    doc_url = models.CharField(max_length=2083)