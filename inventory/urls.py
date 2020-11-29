from django.urls import path

from inventory.api import views

urlpatterns = [  
   
    path('', views.InventoryList.as_view()),
    path('<int:pk>/', views.InventoryDetail.as_view()),
]