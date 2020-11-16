from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):


    patientId       =           models.OneToOneField(User,on_delete=models.CASCADE,related_name='patientId')
    doctorId        =           models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctorId')   
    hospitalName    =           models.CharField(max_length=350)
    treatment       =           models.CharField(max_length=250)   
    date            =           models.DateTimeField(auto_now=False)   

    def __str__(self):
        return "{}".format(self.patientId)
