from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):


    patientId       =           models.OneToOneField(User,on_delete=models.CASCADE,related_name='patientUser')
    doctorId        =           models.TextField(max_length=255,blank=True)
    hospitalName    =           models.TextField(max_length=255,blank=True)
    treatment       =           models.TextField(max_length=255,blank=True)
    date            =           models.TextField(max_length=255,blank=True)  

    def __str__(self):
        return "{}".format(self.patientId)
