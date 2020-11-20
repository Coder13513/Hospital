from django.db import models
from django.db.models.signals import pre_save,post_save

# Create your models here.

class InvoiceDetails(models.Model):

    patientId           =           models.PositiveIntegerField(null=False)
    admitDate           =           models.DateField(null=False)
    releaseDate         =           models.DateField(null=False)
    daySpent            =           models.PositiveIntegerField(null=True,blank=True,)
    roomCharge          =           models.PositiveIntegerField(null=False)
    medicineCost        =           models.PositiveIntegerField(null=False)
    doctorFee           =           models.PositiveIntegerField(null=False)
    OtherCharge         =           models.PositiveIntegerField(null=False)


    def __str__(self):
        return  "{},{}".format(self.patientId,self.releaseDate) 


class PatientDischargeDetails(models.Model):

    patientId           =           models.PositiveIntegerField(null=False)
    admitDate           =           models.DateField(null=True)
    patientName         =           models.CharField(max_length=40)
    assignedDoctorName  =           models.CharField(max_length=40)
    address             =           models.CharField(max_length=40)
    mobile              =           models.CharField(max_length=20,null=True)
    symptoms            =           models.CharField(max_length=100,null=True)   
    total               =           models.PositiveIntegerField(null=False)  


    def __str__(self):
        return '{},{}'.format (self.patientId,self.admitDate) 


    
def post_save_invoiceDetails(instance,sender,*args,**kwrags): 

    patient_admit_date        =       instance.admitDate
    patient_release_date       =      instance.releaseDate  
    days_spent                  =     patient_release_date-patient_admit_date
    print(days_spent.days)
    InvoiceDetails.objects.filter(patientId=instance.patientId ).update(daySpent=days_spent.days)


# post_save.connect(post_save_invoiceDetails,sender=InvoiceDetails)


# def post_save_invoiceDetails(instance,sender,*args,**kwrags): 

    a= instance.patientId
    # b=instance.admitDate
    # print(b)
    sum_values      =   InvoiceDetails.objects.filter(patientId=instance.patientId).values('roomCharge','medicineCost','doctorFee','OtherCharge')
    print(sum_values)
    for i in sum_values:
       a=i['roomCharge']+i['medicineCost']+i['doctorFee']+i['OtherCharge']
       
    total  =a
    print(total)
    PatientDischargeDetails.objects.create(patientId=instance.patientId,admitDate=instance.admitDate,total=total)


post_save.connect(post_save_invoiceDetails,sender=InvoiceDetails)







