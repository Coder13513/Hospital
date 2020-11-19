from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from record.models import Record

# Create your models here.

class History(models.Model):


    patientId       =           models.ForeignKey(User,on_delete=models.CASCADE,related_name='patientUser')
    doctorId        =           models.TextField(max_length=255,blank=True)
    hospitalName    =           models.TextField(max_length=255,blank=True)
    treatment       =           models.TextField(max_length=255,blank=True)
    date            =           models.TextField(max_length=255,blank=True)  

    def __str__(self):
        return "{}".format(self.patientId)



def post_save_history(sender,instance,created,*args, **kwargs):

    patient_id=instance.patientId
    print(patient_id)
  
    objects=Record.objects.filter(patientId=patient_id)
    print(objects)

    dr_id=objects.values_list('doctorId') 
    print(dr_id)
    
    hospital_name=objects.values_list('hospitalName')
    treatment=objects.values_list('treatment')
    date=objects.values_list('date')

    if not instance.doctorId:
        list1 =[]
        for vari in dr_id:
            list1.append(vari)
        History.objects.filter(pk=instance.pk).update(doctorId=list1)
        list2 =[]
        for vari in hospital_name:
            list2.append(vari)
        History.objects.filter(pk=instance.pk).update(hospitalName=list2)
        list3 =[]
        for vari in treatment:
            list3.append(vari)
        History.objects.filter(pk=instance.pk).update(treatment=list3)
        list4 =[]
        for vari in date:
            list4.append(vari)
        History.objects.filter(pk=instance.pk).update(date=list4)



post_save.connect(post_save_history, sender=History)