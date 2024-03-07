from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ProductCrud(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JPO=ProductModelSerializer(LPO,many=True)
        return Response(JPO.data)

    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JPO=ProductModelSerializer(PO)
        return Response(JPO.data)
    
    def create(self,request):
        JD=request.data
        PDO=ProductModelSerializer(data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Created':'Data is inserted'})
        
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Updation Unsuccessful'})
        
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Updation Unsuccessful'})
   
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Data is deleted'})
