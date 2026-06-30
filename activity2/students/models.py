from django.db import models


class PredictionHistory(models.Model):
    demographic = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    weekly_hours = models.FloatField()
    prediction_result = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.demographic} - {self.prediction_result} ({self.created_at.date()})"