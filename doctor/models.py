from django.db import models
from authentication.models import User  

departments=[
('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

# Create your models here.
class Doctor(models.Model):
    user        =       models.OneToOneField(User,on_delete=models.CASCADE)
    name        =       models.CharField(max_length=150)
    address     =       models.CharField(max_length=40)
    mobile      =       models.CharField(max_length=20,null=True)
    specialization  =   models.CharField(max_length=50,choices=departments,default='Cardiologist')
    hospital_name=      models.CharField(max_length=150)
    
    def __str__(self):
        return "{},{}".format(self.user,self.specialization)