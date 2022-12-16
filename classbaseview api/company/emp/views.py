
from django.shortcuts import render
from rest_framework.views import APIView
from.models import employee
from.serializers import empserializer
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.
class employeeapi(APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            emp=employee.objects.get(id=id)
            serializer=empserializer(emp)
            return Response(serializer.data)
        emp=employee.objects.all()
        serializer=empserializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=empserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"reord posted successfully"},status=status.HTTP_202_ACCEPTED)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    def put(self,request,pk):
        id=pk
        emp=employee.objects.get(pk=id)
        serializer=empserializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    def patch(self,request,pk):
        id=pk
        emp=employee.objects.get(pk=id)
        serializer=empserializer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)    
    def delete(self,request,pk):
        id=pk 
        emp=employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'record deleted successfully.....'})           