from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre=models.CharField(max_length=100,default='')
    Likes=models.ManyToManyField(User,blank=True,related_name='likes')
    report=models.ManyToManyField(User,blank=True,related_name='report')

    def __str__(self):
        return self.title
    def get_totol(self):
        return self.Likes.count()

    def get_total_report(self):
        return self.report.count()