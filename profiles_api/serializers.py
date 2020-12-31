from rest_framework import serializers


class PokemonSerializer(serializers.Serializer):
    """Serializer a name field for API view"""
    name = serializers.CharField(max_length=15)
    
