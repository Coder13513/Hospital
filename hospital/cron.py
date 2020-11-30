from django.core.mail import send_mail
from django.utils import timezone
import datetime
from django.core.management.base import BaseCommand, CommandError
from booking.models import Appointment
import os
from crontab import CronTab
from django_cron import CronJobBase, Schedule
from datetime import date


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'hospital.my_cron_job'    # a unique code

    def do(self):
        # do your thing here
        print("cronjob => it run on every minute")  
       
        today = datetime.date.today() 
        print("today date",today)        
        new_today=today.strftime("%Y,%m,%d")
        print("new_today",new_today)
       
        a=Appointment.objects.all()   
        # print(a)
        emailIds=[ b.patientId.email for b in  Appointment.objects.all()] 
        print(emailIds)    
        timestamps=a.values_list('appointmentDate',flat=True)       
        # print(timestamps)       
        date_strings = [d.strftime('%Y,%m,%d') for d in timestamps]
        print(date_strings)       
        length = len(date_strings)
        print(length)
        
        for i in range(length): 
            print(i)
            index=i
            print(index)
            j=date_strings[i]
            # print(j)  
            # print(new_today)       
            if  ( j == new_today) :
                # index = date_strings.index(j)
                # print(index)
                email=emailIds[index]
                print(email)
                subject = 'Schedule reminder'
                body = 'Hey, please complete your schedule ' + schedule.patientName
                send_mail(subject, body, 'amanpreet1052@gmail.com',[email])
                print("mail sent")



        # for schedule in Appointment.objects.all():                               
        #     # print(schedule.patientId.email)
        #     subject = 'Schedule reminder'
        #     body = 'Hey, please complete your schedule ' + schedule.patientName
        #     send_mail(subject, body, 'amanpreet1052@gmail.com',[schedule.patientId.email])
        #     print("mail sent")
