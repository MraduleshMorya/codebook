from email.mime import image
from django.db import models
import datetime
from datetime import *
# from pytz import timezone
import pytz
from  django.utils import timezone,datetime_safe
# Create your models here.

IST = pytz.timezone('Asia/Kolkata')


class posts(models.Model):
    postid = models.BigAutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=150)
    photo = models.ImageField(
        upload_to='posted_images/', null=True, blank=True)
    video = models.FileField(
        upload_to='posted_videos/', null=True, blank=True)
    description = models.TextField(max_length=1500)
    created_at = models.DateTimeField(default=timezone.now())
    catagory = models.CharField(default="image", max_length=6)
    like_count = models.IntegerField(default=0)
    comment_count =models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}{self.postid}"


class notifications(models.Model):
    postid = models.ForeignKey(posts,on_delete=models.CASCADE, null=True, blank=True)
    author_username = models.CharField(max_length=150)
    postid_toshow = models.BigIntegerField(null=True, blank=True)
    friend_username = models.CharField(max_length=150)
    operation = models.CharField(max_length=25)
    
