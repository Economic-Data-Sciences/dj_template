from rest_framework import serializers
from .models import StreamingVariable, StateMetrics

class StreamingVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingVariable
        fields = '__all__'


class StateMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMetrics
        fields = '__all__'