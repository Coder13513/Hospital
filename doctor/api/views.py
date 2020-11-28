from django.shortcuts import render
from rest_framework import  generics,status
from doctor.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

 
class DoctorListAdmin(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser] # (permissions only for if user.is_staff is True)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


 
class DoctorList(generics.GenericAPIView):

    permission_classes = [IsAuthenticated,]   
    serializer_class = DoctorSerializer    
       
    def get(self, request):
        user = self.request.user
        print("logged in doctor id ------------" ,user.id)
        try:
            fav = Doctor.objects.get(user_id=user.id)
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