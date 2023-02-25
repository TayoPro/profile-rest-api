from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.authentication import TokenAuthentication

from . import serializers 
from . import models 
from . import permissions 
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




class HelloViewSet(viewsets.ViewSet):
    """Testing Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message. """

        a_viewset = ['uses actions (list, create, retrieve, update, partial update, destroy)',
                    'Automatically mapps to URLs using Routers',
                    'provides more functionality with less code.'
                    ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            # message = f'Hello {name}'
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handles deleting an object."""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling Creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
