from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from .models import ReverseMortgageInput
from .calculator_utils import calculate_reverse_mortgage

class ReverseMortgageCalculatorTestCase(TestCase):
    def setUp(self):
        self.test_input = ReverseMortgageInput.objects.create(
            age=65,
            property_value=300000,
            current_loan_balance=50000,
            margin=3.4
        )

    def test_reverse_mortgage_calculation(self):
        age = self.test_input.age
        property_value = self.test_input.property_value
        current_loan_balance = self.test_input.current_loan_balance
        margin = self.test_input.margin
        expected_result = calculate_reverse_mortgage(age, property_value, current_loan_balance, margin)
        self.assertAlmostEqual(expected_result, Decimal(27690.05102040816251543463099), places=2)

    def test_reverse_mortgage_view(self):
        response = self.client.post(reverse('ReverseMortgageCalculatorView'), {
            'age': 65,
            'property_value': 300000,
            'current_loan_balance': 50000,
            'margin': 3.5
        })
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result:  28536.13945578231292704700367')
