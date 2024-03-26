import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField('title', max_length = 200)
    description = models.TextField('description text')
    date_created = models.DateTimeField('date created', auto_now_add=True)
    checked = models.BooleanField('checked', default=False, null=True, blank=True)
    date_start = models.DateTimeField('date start', default=None, null=True, blank=True)
    date_end = models.DateTimeField('date end', default=None, null=True, blank=True)
    date_time = models.DateTimeField('date time', default=None, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))