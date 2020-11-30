from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
import datetime
from django.core.management.base import BaseCommand, CommandError
from booking.models import Appointment
import os
from crontab import CronTab

class Command(BaseCommand):
    print("cronjob")
    def handle(self, **options):
        today = datetime.datetime.now().date()
        today = datetime.date.today()
        print(datetime.datetime.now().date())
        for schedule in Appointment.objects.filter(appointmentDate=today):
            print(schedule.patientId.email)
            subject = 'Schedule reminder'
            body = 'Hey, please complete your schedule ' + schedule.patientName
            send_mail(subject, body, 'amanpreet1052@gmail.com',
                      [schedule.patientId.email])