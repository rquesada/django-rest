from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")
    else:
        return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    activate = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.activate = validated_data.get('activate', instance.activate)
        instance.save()
        return instance
    
    #Validation Object Level
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        else:
            return data
        
    
    #Validation Field Level
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
