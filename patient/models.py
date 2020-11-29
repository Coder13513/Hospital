from django.db import models
from authentication.models import User  


# Create your models here.
class Patient(models.Model):
    user                    =           models.OneToOneField(User,on_delete=models.CASCADE)  
    address                 =           models.CharField(max_length=40)
    mobile                  =           models.CharField(max_length=20,null=False)
    symptoms                =           models.CharField(max_length=100,null=False)
    assignedDoctorId        =           models.PositiveIntegerField(null=True)
    admitDate               =           models.DateField(auto_now=True)
    
   
   
    def __str__(self):
        return self.user.username