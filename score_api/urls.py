from django.urls import path
from . import views

urlpatterns = [
    path('get_score/', views.get_score, name='get_score'),
]
