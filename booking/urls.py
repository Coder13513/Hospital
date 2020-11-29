from django.urls import path
from booking.api import views

urlpatterns = [  
  
    path('', views.AppointmentList.as_view()),
    path('<int:pk>/', views.AppointmentDetail.as_view()),
    # for doctors to view their appointments
    path('doctor/', views.AppointmentListDoctor.as_view()),
]