# forms.py
from django import forms
from calculator.models import ReverseMortgageInput

class ReverseMortgageForm(forms.ModelForm):
    class Meta:
        model = ReverseMortgageInput
        fields = ['age', 'property_value', 'current_loan_balance', 'margin']
