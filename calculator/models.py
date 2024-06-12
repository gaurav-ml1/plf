# models.py
from django.db import models

class ReverseMortgageInput(models.Model):
    CATEGORY_CHOICES = [
        (3.5, 3.5),
        (4.5, 4.5),
        (2.3, 2.3),
    ]
    margin = models.DecimalField(max_digits=10, decimal_places=2, choices=CATEGORY_CHOICES)
    age = models.IntegerField()
    property_value = models.DecimalField(max_digits=10, decimal_places=2)
    current_loan_balance = models.DecimalField(max_digits=10, decimal_places=2)



