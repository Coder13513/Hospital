from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.

choices=[('Confirmed','confirmed'),('Pending','pending')]

class Appointment(models.Model):
    patientId         =               models.OneToOneField(User,on_delete=models.CASCADE,related_name='patientID')
    doctorId          =               models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctorID')
    patientName       =               models.CharField(max_length=40)
    doctorName        =               models.CharField(max_length=40)
    appointmentDate   =               models.DateTimeField(auto_now=False)
    status            =               models.CharField(max_length=20,choices=choices,default='Pending',)



    def __str__(self):
        # return self.patientName
        return "{} ,{}".format(self.patientName,self.appointmentDate)


def post_save_appointment(sender,instance,created,*args, **kwargs):

    print("print from postsave function")
    foos = Appointment.objects.all()
    for foo in foos: 
        if foo.appointmentDate < timezone.now():
            foo.delete() 
            print(timezone.now())  

post_save.connect(post_save_appointment, sender=Appointment)