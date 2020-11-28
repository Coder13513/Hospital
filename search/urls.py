from django.urls import path
from search.api import views

urlpatterns = [
   
    path('', views.SearchList.as_view()),
]