from django.urls import path
from booking.api import views

urlpatterns = [  
  
    path('', views.AppointmentList.as_view()),
    path('<int:pk>/', views.AppointmentDetail.as_view()),
]