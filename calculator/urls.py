from django.urls import path
from calculator.views import ReverseMortgageCalculatorView

urlpatterns = [
    path('loan', ReverseMortgageCalculatorView.as_view(), name='ReverseMortgageCalculatorView')
]
