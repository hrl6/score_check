from django.db import models

class ScoreLog(models.Model):
    user_id = models.CharField(max_length=100)
    input_value = models.FloatField()
    output_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Score for user {self.user_id}: {self.output_score}"
