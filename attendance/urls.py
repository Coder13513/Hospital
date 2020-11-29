from django.urls import path
from attendance.api import views

urlpatterns = [  
  
    path('doctor/', views.DoctorList.as_view()),
    path('doctor/<int:pk>/', views.DoctorDetail.as_view()),
    path('staff/', views.StaffList.as_view()),
    path('staff/<int:pk>/', views.StaffDetail.as_view()),
    
]