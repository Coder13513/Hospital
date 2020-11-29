from django.urls import path

from history.api import views

urlpatterns = [  
   
    path('', views.HistoryList.as_view()),
    path('<int:pk>/', views.HistoryDetail.as_view()),
]