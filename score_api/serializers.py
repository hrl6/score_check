from rest_framework import serializers
from .models import ScoreLog

class ScoreLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreLog
        fields = ['user_id', 'input_value', 'output_score', 'timestamp']