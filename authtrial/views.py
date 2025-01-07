from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import userSerializer,noteSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note

class noteCreate(generics.ListCreateAPIView):
    serializer_class=noteSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.error)
            
class noteDelete(generics.DestroyAPIView):
    serializer_class=noteSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)




class createUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer
    permission_classes=[AllowAny]
