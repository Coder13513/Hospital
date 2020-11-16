
from django.core.management.base import BaseCommand, CommandError
from booking.models import Appointment
from django.utils import timezone

class Command(BaseCommand):
    help = 'Type the help text here'


    # def hi():
    def handle(self, *args, **options):
        print("print from cron tab")
        foos = Appointment.objects.all()
        for foo in foos: 
            if foo.appointmentDate < timezone.now():
                foo.delete()

    # def handle(self, *args, **options):
    #     # Add yout logic here
    #     # This is the task that will be run
    #     print("cron run")
    #     foos = Appointment.objects.all()
    #     for foo in foos:       

    #     # If the expiration date is bigger than now delete it
    #         if foo.appointmentDate < timezone.now():
    #             foo.delete()
    #         # log deletion


        



        self.stdout.write('This was extremely simple!!!')