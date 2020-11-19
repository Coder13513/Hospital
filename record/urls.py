from django.urls import path

from record import views

urlpatterns = [
   
   
    path('', views.List.as_view()),
]