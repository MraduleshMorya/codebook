from typing_extensions import Required
from rest_framework import serializers
from django.db import models
from setuptools import Require
from .models import invoke_detail


class invoke_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoke_detail
        fields = '__all__'
