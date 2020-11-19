from django.urls import path

from history import views

urlpatterns = [  
   
    path('', views.List.as_view()),
]