import email
from email.policy import default
from pyexpat import model
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

from codebook_posts.models import posts
# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=150, primary_key=True, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    profile_pic = models.ImageField(upload_to='images/', default= 'images/profile_pic_default.png')
    birth_date = models.DateField()
    about = models.CharField(max_length=500, blank=True, default="its my about section")
    
    def __str__(self):
        return str(self.username)
    
    
    
class User_model(models.Model):
    username = models.CharField(max_length=150, primary_key=True, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    profile_pic = models.ImageField(
        upload_to='images/', default='images/profile_pic_default.png')
    birth_date = models.DateField()
    about = models.CharField(max_length=500, blank=True, default="its my about section")
    
    def __str__(self):
        return str(self.username)


class friends2(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    friend_with = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    temp = models.AutoField(primary_key=True, unique=True,)
    def __str__(self):
        return str(self.username)
    
    
class liked_posts(models.Model):
    postid = models.ForeignKey(posts, on_delete=models.CASCADE,null=True, blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return str(self.username)
    
    
class post_commnets(models.Model):
    postid = models.ForeignKey(
        posts, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    comment = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.username}{self.postid}"
    
    

