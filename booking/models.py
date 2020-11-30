from django.db import models
from authentication.models import User 
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import date
import datetime
from django.core.mail import send_mail

# Create your models here.

choices=[('Confirmed','confirmed'),('Pending','pending')]

class Appointment(models.Model):
    patientId         =               models.ForeignKey(User,on_delete=models.CASCADE,related_name='patientID')
    doctorId          =               models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctorID')
    patientName       =               models.CharField(max_length=40)
    doctorName        =               models.CharField(max_length=40)
    appointmentDate   =               models.DateTimeField(auto_now=False)
    status            =               models.CharField(max_length=20,choices=choices,default='Pending',)



    def __str__(self):
        # return self.patientName
        return "{} ,{}".format(self.patientName,self.appointmentDate)


def post_save_appointment(sender,instance,created,*args, **kwargs):


    print("print from postsave function")   
   
    today = datetime.datetime.now().date()
    print("shows today date",today)
    # print(timezone.now()+ timezone.timedelta(days=1))

    foos = Appointment.objects.all()
   
    for foo in foos: 
        # send_mail(
        #                  'reminder',    'visit for your appointment.','amanpreet1052@gmail.com',
        #                    ['amanpreet.leanvia@outlook.com'],)
       
        if foo.appointmentDate < timezone.now():
            print('deleted')
            foo.delete() 
            
             

post_save.connect(post_save_appointment, sender=Appointment)