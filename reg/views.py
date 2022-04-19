from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from reg.models import Register
from reg.serializers import RegisterSerializer
import hashlib, uuid


class UserView(ViewSet):


    def list(self, request):
        try:
            queryset = Register.objects.all()
            serializer = RegisterSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": True, "message": str(e), "status": 400}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):

        # serializer = RegisterSerializer(data=request.data)
        # data = {}
        # if serializer.is_valid():
            
        #     account = serializer.save()
        #     data['response'] = "successfully registered a new user."
        #     data['email'] = account.email
        #     data['username'] = account.username
        # else:
        #     data = serializer.errors
        # return Response(data)

        try:
        
            if request.data['password1'] != request.data['password2']:
                 return Response({"error": False, "message": "password does't match   is Missing ",
                                 "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
            if request.data['password1'] == request.data['password2'] :
                query_set = Register.objects.filter(username=request.data['username'])
                if query_set:
                    return Response({"error": False, "message": "username_name  already exists ",
                                     "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            #password = hashlib.sha1(request.data['password1'])
            serserializers = RegisterSerializer(data=request.data)
            serserializers.is_valid(raise_exception=True)
            serserializers.save()
            response_content = {"error": False, "message": "Successfully Register", "status": 200, }
            return Response(response_content, status=status.HTTP_200_OK)
        
        except Exception as e:
            
           return Response({"error": True, "message": str(e), "status": 400}, status=status.HTTP_400_BAD_REQUEST)

    def login_user(self , request):
        
        username = request.data['username']
        password1 = request.data['password']
        account = Register.objects.filter(username = username).filter(password1 = password1)
        if account:
            response_content = {"error": False, "message": "Success login", "status": 200, }
            return Response(response_content, status=status.HTTP_200_OK)
        else : 
           return Response({"error": True, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        

    def update(self,  request):
        password1 = request.data['password1']
        password2 = request.data['password2']
        if password1==password2:
            query_set = Register.objects.filter(username=request.data['username'])
            if query_set:
                data1 = Register.objects.get(username=request.data['username'])
                data1.password1 = request.data.get('password1',data1.password1)
                data1.password2 = request.data.get('password2',data1.password2)
                data1.save()
                serializer = RegisterSerializer(data1)
                return Response({"error": False, "message": "user updated successfully", "status": 200 , "data":serializer.data}, status=status.HTTP_200_OK)
            else : 
                return Response({"error": True, "message": "username does't exit", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        else : 
                return Response({"error": True, "message": "password should be equal", "status": 400}, status=status.HTTP_400_BAD_REQUEST)