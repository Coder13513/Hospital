from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from search import views

urlpatterns = [
   
    # path('teacher/', views.teacherAPIView.as_view()),
    # path('teacher/<int:pk>/', views.teacherDetail.as_view()),
    path('', views.List.as_view()),
]