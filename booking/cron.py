from django.utils import timezone
from booking.models import Appointment


def hi(self, *args, **options):
    print("print from cron tab")
    foos = Appointment.objects.all()
    for foo in foos: 
        if foo.appointmentDate < timezone.now():
            foo.delete()
    # f= open('/Home/Desktop/aman.txt','w')
    # f.close()