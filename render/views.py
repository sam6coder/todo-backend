from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework import generics
from .models import Todo
from rest_framework.response import Response

# Create your views here.

class TodoGetCreate(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    
    
    
class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    
    # def update(self,request,*args,**kwargs):
    #     instance=self.get_object()
    #     partial=kwargs.pop('partial',False)
        
    #     data=request.data
    #     if 'status' in data and data['status']=='Completed':
    #         data['completed_at']='2024-11-21'
    #     serializer=self.get_serializer(instance,data=data,partaial=partial)
    #     if serializer.is_valid():
    #         self.perform_update(serializer)
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def destroy(self, request, *args, **kwargs):
    #     instance=self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(
    #         {'message': 'Todo deleted successfully'},
    #         status=status.HTTP_204_NO_CONTENT
    #     )
