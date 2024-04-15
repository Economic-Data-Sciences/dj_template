from rest_framework import serializers
from .models import StreamingVariable 

class StreamingVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingVariable
        fields = '__all__'