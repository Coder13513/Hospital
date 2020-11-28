from django.urls import path
from doctor.api import views

urlpatterns = [
   
     #  for Admin only 
    path('adminList/', views.DoctorListAdmin.as_view()),
    path('adminDetail/<int:pk>/', views.DoctorDetailAdmin.as_view()),
    # for doctors  to view own profile
    path('', views.DoctorList.as_view()),    

]