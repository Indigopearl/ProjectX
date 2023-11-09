# finance/models.py
from django.db import models

class StockEvent(models.Model):
    date = models.DateField()
    eps_actual = models.FloatField()
    eps_estimate = models.FloatField()
    revenue_actual = models.BigIntegerField()
    revenue_estimate = models.BigIntegerField()
    symbol = models.CharField(max_length=50)
