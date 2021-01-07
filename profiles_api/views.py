from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers


class TestViewSet(viewsets.ViewSet):
    """test ViewSet"""

    serializer_class = serializers.PokemonSerializer

    def list(self, request):
        """return list of pokemons"""

        pokemons = [
            'Charizard',
            'Onyx',
            'Jigglypuff'
        ]
        return Response({'message':'Pokemons', 'pokemons':pokemons})

    def create(self, request):
        """Create hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by its ID"""
        return Response({'method':'GET'})


    def update(self, request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating object partially"""
        return Response({'method':'PATHCH'})

    def destroy(self, request, pk=None):
        """Handle deleting the object"""
        return Response({'method':'DELETE'})


class TestApiView(APIView):
    """Test API View"""

    serializer_class = serializers.PokemonSerializer

    def get(self, request, format=None):
        """Returns list of items"""
        list_of_pokemons = [
            'Pikachu',
            'Bulbasaur',
            'Charmander',
            'Squirtle'
        ]
        return Response({'list_of_pokemons':list_of_pokemons})

    def post(self, request):
        """Create a Hello message with Pokemon name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """Handle updating entire object"""
        return Response({'message': 'PUT method is being used!'})

    def patch(self, request, pk=None):
        """Handle single element in the object"""
        return Response({'message': 'PATCH method is used'})

    def delete(self, request, pk=None):
        """Handle delete object"""
        return Response({'message': 'DELETE is used'})
