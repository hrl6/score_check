from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import ScoreLog

class ScoreAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_valid_score_calculation(self):
        """Test the score calculation with valid input"""
        data = {
            'user_id': 'test_user',
            'input_value': 5.0
        }
        
        response = self.client.post(reverse('get_score'), data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['output_score'], 6.0)  # to check correct output
        self.assertEqual(ScoreLog.objects.count(), 1)
        
    def test_invalid_input(self):
        """Test the API with invalid input"""
        data = {
            'user_id': 'test_user',
            'input_value': 'invalid'
        }
        
        response = self.client.post(reverse('get_score'), data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ScoreLog.objects.count(), 0)
