from django.db import models 
from django.contrib.auth.models import User  

# Create your models here.
class Staff(models.Model):

    user        =       models.OneToOneField(User,on_delete=models.CASCADE)
    address     =       models.CharField(max_length=40)
    mobile      =       models.CharField(max_length=20,null=True)
    designation =       models.CharField(max_length=150)
    hospital_name=      models.CharField(max_length=150)
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.designation)