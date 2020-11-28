from django.urls import path
from patient.api import views

urlpatterns = [
  
  
  #  for Admin only 
    path('adminList/', views.PatientListAdmin.as_view()),
    path('adminDetail/<int:pk>/', views.PatientDetailAdmin.as_view()),
    # for patients  to view own profile
    path('', views.PatientList.as_view()), 

]