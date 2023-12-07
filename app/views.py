from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def host(request):
    if request.method=='GET':
        PO=Employe.objects.all()
        JSO=EmployeMS(PO,many=True)
        return Response(JSO.data)
    elif request.method=="POST":
        JPO=EmployeMS(data=request.data)
        if JPO.is_valid():
            JPO.save()
            return Response({'message':'insertion is done'})
        return Response({'message':'invalid data'})
