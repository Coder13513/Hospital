from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
import datetime
from django.core.management.base import BaseCommand, CommandError
from booking.models import Appointment
import os
from crontab import CronTab

class Command(BaseCommand):
    help = 'Cron testing'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #init cron
        cron = CronTab(user='aman')

        #add new cron job
        job = cron.new(command='python <django/leanvia_projects/hospital/booking/management>/example.py >>/tmp/out.txt 2>&1')

        #job settings
        job.minute.every(1)

        cron.write()


# class Command(BaseCommand):
#     print("cronjob")
#     def handle(self, **options):
#         today = datetime.datetime.now().date()
#         today = datetime.date.today()
#         print(datetime.datetime.now().date())
#         for schedule in Appointment.objects.filter(appointmentDate=today):
#             print(schedule.patientId.email)
#             subject = 'Schedule reminder'
#             body = 'Hey, please complete your schedule ' + schedule.patientName
#             send_mail(subject, body, 'amanpreet1052@gmail.com',
#                       [schedule.patientId.email])

# class Command(BaseCommand):
#     help = 'Type the help text here'

#     # def hi():
#     def handle(self, *args, **options):
#         print("print from cron tab")
#         foos = Appointment.objects.all()
#         for foo in foos: 
#             if foo.appointmentDate < timezone.now():
#                 foo.delete()

#     # def handle(self, *args, **options):
#     #     # Add yout logic here
#     #     # This is the task that will be run
#     #     print("cron run")
#     #     foos = Appointment.objects.all()
#     #     for foo in foos:       

#     #     # If the expiration date is bigger than now delete it
#     #         if foo.appointmentDate < timezone.now():
#     #             foo.delete()
#     #         # log deletion
    
#         self.stdout.write('This was extremely simple!!!')

