from decimal import Decimal



def calculate_reverse_mortgage(age, property_value, current_loan_balance, margin):
    # Constants for calculation
    max_loan_to_value_ratio = 0.5  
    interest_rate = 0.05  # Annual interest rate (for example)
    loan_term_years = 30  
    upfront_mip_rate = 0.02  
    annual_mip_rate = 0.005  
    servicing_fee_rate = 0.005  
    max_loan_age_threshold = 80  #Age threshold for maximum loan amount adjustment

    if age >= max_loan_age_threshold:
        max_loan_to_value_ratio = 0.6  

    max_loan_amount = property_value * Decimal(max_loan_to_value_ratio)

    remaining_loan_balance = max_loan_amount - current_loan_balance

    monthly_interest_rate = (Decimal(interest_rate) + Decimal(margin)) / 12

    loan_term_months = loan_term_years * 12

    principal_limit = remaining_loan_balance / ((1 - (1 + monthly_interest_rate) ** -loan_term_months) / Decimal(monthly_interest_rate))

    principal_limit *= 1 / (1 - Decimal(upfront_mip_rate))

    principal_limit *= (1 - Decimal(servicing_fee_rate))

    principal_limit -= property_value * Decimal(annual_mip_rate)

    return principal_limit
