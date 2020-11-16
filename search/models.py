from django.db import models
from doctor.models import Doctor
from django.db.models.signals import post_save

# Create your models here
departments=[
('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Search(models.Model):
    specialization  =       models.CharField(max_length=50,choices=departments,default='Cardiologist')
    doctors         =       models.TextField(max_length=255,blank=True)
    hospital        =       models.TextField(max_length=255,blank=True)


    def __str__(self):
        return str(self.doctors)

def post_save_search(sender,instance,created,*args, **kwargs):

    a=instance.specialization
    print(a)
    s=Doctor.objects.all()
    box=s.filter(specialization=a)
    print(box)
    i = box.values_list('name')
    t = box.values_list('hospital_name')
    # j=  box.values_list('User.first_name')
    # print(j)
    print(i)
    if not instance.doctors:
        lst =[]
        for vari in i:
            lst.append(vari)
        Search.objects.filter(pk=instance.pk).update(doctors=lst)
        lst2=[]
        for var in t:
            lst2.append(var)
        Search.objects.filter(pk=instance.pk).update(hospital=lst2)

post_save.connect(post_save_search, sender=Search)
