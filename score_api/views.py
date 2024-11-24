from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ScoreLog
from .serializers import ScoreLogSerializer

@api_view(['POST'])
def get_score(request):
    try:
        user_id = request.data.get('user_id')
        input_value = float(request.data.get('input_value'))
        
        # formula
        output_score = input_value + 1
        
        score_log = ScoreLog.objects.create(
            user_id=user_id,
            input_value=input_value,
            output_score=output_score
        )
        
        serializer = ScoreLogSerializer(score_log)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except (TypeError, ValueError):
        return Response(
            {'error': 'Invalid input. Check your user_id and input_value.'},
            status=status.HTTP_400_BAD_REQUEST
        )
