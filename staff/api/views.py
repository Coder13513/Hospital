from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import  generics,status
from staff.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

 
class StaffListAdmin(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser] # (permissions only for if user.is_staff is True)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


 
class StaffList(generics.GenericAPIView):

    permission_classes = [IsAuthenticated,]   
    serializer_class = StaffSerializer    
       
    def get(self, request):
        user = self.request.user
        print("logged in staff id ------------" ,user.id)
        try:
            fav = Staff.objects.get(user_id=user.id)
            serializer = self.serializer_class(fav)
            response = {
                'data' : serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {
                'message': 'Please Login'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 