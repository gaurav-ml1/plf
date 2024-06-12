# views.py
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import ReverseMortgageForm
from .calculator_utils import calculate_reverse_mortgage


class ReverseMortgageCalculatorView(FormView):
    template_name = 'calculator/form.html'
    form_class = ReverseMortgageForm

    def form_valid(self, form):
        age = form.cleaned_data['age']
        property_value = form.cleaned_data['property_value']
        current_loan_balance = form.cleaned_data['current_loan_balance']
        margin = form.cleaned_data['margin']
        result = calculate_reverse_mortgage(age, property_value, current_loan_balance, margin)
        return render(self.request, 'calculator/result.html', {'result': result, "form": form})
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.GET)
        if request.GET:
            age = request.GET['age']
            property_value = request.GET['property_value']
            current_loan_balance = request.GET['current_loan_balance']
            margin = request.GET['margin']
            result = calculate_reverse_mortgage(age, property_value, current_loan_balance, margin)
            return HttpResponse(result)
        return render(self.request, 'calculator/form.html', {"form": self.form_class})
