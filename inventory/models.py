from django.db import models

# Create your models here.

# choices =   (
#       ('AVAILABLE', 'Item ready to be purchased'),
#       ('SOLD', 'Item already purchased'),
#       ('RESTOCKING', 'Item restocking in few days')
#     )

class stock(models.Model):

    name                =       models.CharField(max_length=250,unique=True)
    price               =       models.IntegerField() 
    scount               =       models.IntegerField()

    def __str__(self):
        return '{0} , {1}'.format(self.name, self.scount)


# class MF(models.Model):

#     name      =       models.CharField(max_length=200, blank=False) 
#     price     =       models.IntegerField()   
#     status    =       models.CharField(max_length=10, choices=choices)
#     issues    =       models.CharField(max_length=50, default="No Issues")
   

    # def __str__(self):
    #     return 'Type: {0} Price: {1}'.format(self.name, self.price)