from django import forms
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from .models import user,User_model
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
        

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username', 'phone_no', 'birth_date']
        
        
class userimageSerializer(forms.ModelForm):
    class Meta:
        model = user
        fields = ["profile_pic"]
        
        
class User_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_model
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'phone_no', 'birth_date']
