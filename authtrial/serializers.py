from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class  userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        extra_kwargs={"password":{"write_only":True}}
        
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class noteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","author","create_at"]
        extra_kwargs={"author":{"read_only":True}}
        
    def create(self,data):
        note=Note.objects.create(**data)
        return note