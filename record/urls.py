from django.urls import path
from record.api import views

urlpatterns = [  
   
    path('', views.RecordList.as_view()), 
    path('<int:pk>/', views.RecordDetail.as_view()),
]