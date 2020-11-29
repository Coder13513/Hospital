from django.urls import path
from discharge.api import views


urlpatterns = [  
  
    path('', views.DischargeList.as_view()),
    path('<int:pk>/', views.DischargeDetail.as_view()),
   
]