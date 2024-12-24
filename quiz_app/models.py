from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class questions(models.Model):
    question=models.CharField(max_length=200)
class options(models.Model):
    question=models.ForeignKey(questions,related_name='options',on_delete=models.CASCADE)
    option=models.CharField(max_length=50)
    is_true=models.BooleanField(default=False)
    
    
