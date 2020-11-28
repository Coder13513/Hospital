from django.urls import path
from staff.api import views

urlpatterns = [
  
  
  #  for Admin only 
    path('adminList/', views.StaffListAdmin.as_view()),
    path('adminDetail/<int:pk>/', views.StaffDetailAdmin.as_view()),
    # for staff  to view own profile
    path('', views.StaffList.as_view()), 

]