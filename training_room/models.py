from django.db import models

# Create your models here.

class TrainingBlock(models.Model):
     name = models.CharField(max_length=30)
     duration = models.IntegerField()
     if_ended = models.BooleanField()
