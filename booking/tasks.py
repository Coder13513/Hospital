from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

@periodic_task(run_every=crontab(minute='*/2'))
def delete_old_foos():
    # Query all the foos in our database
    foos = Appointment.objects.all()

    # Iterate through them
    for foo in foos:
        print("enter_celery")

        # If the expiration date is bigger than now delete it
        if foo.appointmentDate < timezone.now():
            foo.delete()
            # log deletion


    return "completed deleting foos at {}".format(timezone.now())