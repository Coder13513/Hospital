from django.db import models
from doctor.models import *
from staff.models import *

# Create your models here.
class AttendanceDoctors(models.Model):

    email_id_take_attendance        =       models.EmailField(max_length=250)
    doctor                          =       models.ManyToManyField(Doctor)
    attendance_date                 =       models.DateTimeField()

    def __str__(self):
        return "{},{}".format(self.email_id_take_attendance,self.attendance_date)

    
class AttendanceStaff(models.Model):

    email_id_take_attendance        =       models.EmailField(max_length=250)
    staff                          =       models.ManyToManyField(Staff)
    attendance_date                 =       models.DateTimeField()

    def __str__(self):
        return "{},{}".format(self.email_id_take_attendance,self.attendance_date)


