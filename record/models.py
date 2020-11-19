from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from inventory.models import stock


class Record(models.Model):


    patientId       =           models.ForeignKey(User,on_delete=models.CASCADE,related_name='patientId')
    doctorId        =           models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctorId') 
    # doctorName       =           models.CharField(max_length=250)  
    hospitalName    =           models.CharField(max_length=350)
    treatment       =           models.CharField(max_length=250)
    medicines       =           models.CharField(max_length=250)  
    dcount           =           models.IntegerField() 
    date            =           models.DateTimeField(auto_now=False)   

    def __str__(self):
        return "{}".format(self.patientId)




# def post_save_record(sender,instance,created,*args, **kwargs): 

#     patient_id=instance.patientId.username
#     print(patient_id)
#     if instance.patientId:
#         Record.objects.filter(pk=instance.pk).update(patientId=patient_id)

# post_save.connect(post_save_record, sender=Record)


def post_save_record(sender,instance,created,*args, **kwargs): 

    medicine_name           =     instance.medicines
    print(medicine_name)

    record_count             =     instance.dcount
    print(record_count)

    mfs                     =     stock.objects.filter(name=medicine_name)
    print(mfs)

    
    result_list             =       mfs.values('scount')
    print(result_list)

    for item in result_list:
        test=item['scount']
    print(test)
   
  
    c=test-record_count
    print(c)
    
    stock.objects.filter(name=medicine_name).update(scount=c)

post_save.connect(post_save_record, sender=Record)