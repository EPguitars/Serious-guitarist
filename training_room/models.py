from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class TrainingBlock(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     name = models.CharField(max_length=30)
     duration = models.IntegerField(default=0)
     if_ended = models.BooleanField(default=False)

     def __str__(self):
          return self.name


