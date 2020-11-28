from django.shortcuts import render
from rest_framework import  generics,status
from patient.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

 
class PatientListAdmin(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser] # (permissions only for if user.is_staff is True)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


 
class PatientList(generics.GenericAPIView):

    permission_classes = [IsAuthenticated,]   
    serializer_class = PatientSerializer    
       
    def get(self, request):
        user = self.request.user
        print("logged in patient id ------------" ,user.id)
        try:
            fav = Patient.objects.get(user_id=user.id)
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