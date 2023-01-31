from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.



class TrainingBlock(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     name = models.CharField(max_length=20)
     duration = models.IntegerField(default=10)
     if_ended = models.BooleanField(default=False)
     created = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.name

     def get_absolute_url(self):
           pass

