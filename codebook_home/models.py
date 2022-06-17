from pyexpat import model
from django.db import models
from django.utils import timezone, datetime_safe
# Create your models here.


# model to store info regarding the api hits 

class invoke_detail(models.Model):
    username = models.CharField(max_length=150,null=True,blank=True)
    invoked_api = models.CharField(max_length=30,null=True,blank=True)
    invokation_method = models.CharField(max_length=10,null=True,blank=True)
    invoke_date_time = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    request_headers = models.JSONField(null=True)
    
    def __str__(self):
        return self.username
