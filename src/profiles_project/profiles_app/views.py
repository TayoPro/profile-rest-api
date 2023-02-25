from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

from . import serializers 
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView featured."""

        an_apiview= [
            'Uses HTTP methods as function(get, post, put, patch and delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """creates a hello message with our name."""
        serializer = serializers.HelloSerializer(data= request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'message': 'put'})
  
    def patch(self, request, pk=None):
        """patch request, only updates the fields provided in the request object."""

        return Response({'message': 'patch'})


    def delete(self, request, pk=None):
        """deletes an object."""

        return Response({'message': 'delete'})