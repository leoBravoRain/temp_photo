from rest_framework import serializers
from .models import Photo

	
# Serializer of dangers
class Photo_Serializer(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Photo
        # fields = ('id', 'latitude', 'longitude', 'comment','state','photo','date')
        fields = '__all__'