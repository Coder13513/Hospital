from django.shortcuts import render
from rest_framework import  generics,status
from booking.models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)


class AppointmentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer


class  AppointmentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset =  Appointment.objects.all()
    serializer_class =  AppointmentDetailSerializer



class AppointmentListDoctor(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]   
    serializer_class = AppointmentListSerializer   
      
    def get(self, request):
        user = self.request.user
        print("logged in doctor id ------------" ,user.id)
        try:
                    
            fav = Appointment.objects.filter(doctorId_id=user.id)
            serializer = self.serializer_class(fav,many=True)
            response = {
                'data' : serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {
                'message': 'Please Login'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# class  AppointmentDelete(generics.RetrieveUpdateDestroyAPIView):
   
#     serializer_class =  AdminAppointmentSerializer

#     def delete(self, request, *args, **kwargs):
#         queryset =  Appointment.objects.filter(status="Visited")
#         # print Appointment.objects.filter(appointmentDate__lt=datetime.now()).delete()    

#         return self.destroy(request, *args, **kwargs)