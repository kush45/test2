from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reg.models import Register
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):

    # class Meta:
    #     model = Register
    #     fields = '__all__'

    # def save(self):
    #     account = Register(
    #         email=self.validated_data['email'],
    #         username=self.validated_data['username'],
    #     )
    #     password1 = self.validated_data['password1']
    #     password2 = self.validated_data['password2']
        
    
    #     if password1 != password2:
    #         raise serializers.ValidationError({'password': 'Passwords do not match!'})
    
    #     #account.set_password(password1)
    #     account.save()
    #     return account




