from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
