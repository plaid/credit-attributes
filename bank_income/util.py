from datetime import date, timedelta
from plaid.model.credit_bank_income import CreditBankIncome
from plaid.model.credit_bank_income_source import CreditBankIncomeSource

"""
get_total_amount_for_date_range calculates the total amount for 
an income source within a given start and end date
"""


def get_total_amount_for_date_range(
    income_source: CreditBankIncomeSource,
    start_date: date,
    end_date: date,
) -> float:
    total_amount = 0.0
    for historical_summary in income_source.historical_summary:
        if "transactions" not in historical_summary:
            continue
        for transaction in historical_summary.transactions:
            if transaction.date >= start_date and transaction.date <= end_date:
                total_amount += transaction.amount
    return total_amount
