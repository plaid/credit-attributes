from typing import List
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


"""
get_total_amount_for_date_range returns the "active" income sources
that should be used in the monthly average income calculation
"""


def get_active_sources(
    report: CreditBankIncome,
    active_source_window: int,
    categories_to_include: List[str],
) -> List[CreditBankIncomeSource]:
    active_window_end_date = date.today()
    active_window_start_date = active_window_end_date - timedelta(active_source_window)
    active_sources = []

    for bank_income_item in report.items:
        for source in bank_income_item.bank_income_sources:
            # If source has an excluded category, then ignore it
            if str(source.income_category) not in categories_to_include:
                continue
            # Check if source has at least one transaction within the active window or
            # is a TAX_REFUND
            if (
                source.end_date >= active_window_start_date
                or str(source.income_category) == "TAX_REFUND"
            ):
                active_sources.append(source)
    return active_sources


"""
source_monthly_avg_net_income returns the monthly average net income
for an income source across a given averaging window
"""


def source_monthly_avg_net_income(
    source: CreditBankIncomeSource,
    active_source_window: int,
    avg_calculation_window: int,
    AVG_DAYS_MONTH=30.4167,
) -> float:
    active_window_end_date = date.today()
    active_window_start_date = active_window_end_date - timedelta(active_source_window)

    avg_window_end_date = date.today()
    avg_window_start_date = avg_window_end_date - timedelta(avg_calculation_window)

    if str(source.income_category) == "TAX_REFUND":
        # For tax refund, amortize the amount evenly over the year
        return source.total_amount / 12
    elif source.start_date >= active_window_start_date:
        # For new jobs that started within the active window, average amount over the active window to get a
        # daily average and multiply by the AVG_DAYS_MONTH multiple
        return source.total_amount / active_source_window * AVG_DAYS_MONTH
    elif source.start_date >= avg_window_start_date:
        # For jobs that started within the averaging window, average amount since the start date to get a daily average
        # and multiply by the AVG_DAYS_MONTH multiple
        return (
            source.total_amount
            / (avg_window_end_date - source.start_date).days
            * AVG_DAYS_MONTH
        )
    else:
        # For jobs that have been ongoing, average amount over the avg_calculation_window to get a daily average
        # and multiply by the AVG_DAYS_MONTH multiple
        amount_in_avg_window = get_total_amount_for_date_range(
            source, avg_window_start_date, avg_window_end_date
        )
        return amount_in_avg_window / avg_calculation_window * AVG_DAYS_MONTH


"""
get_gross_income_from_net_income estimates gross income from a net income
value for a given category
"""


def get_gross_income_from_net_income(
    amount: float,
    category: str,
) -> float:
    # If the income is from salary, multiply by a 1.25x multiplier to account for taxes.
    # Institutions like FreddieMac recommend multiplying by 1.25, which represents a general 25% tax
    # rate in the United States and is typically the standard used by government-sponsored enterprises.
    if category == "SALARY":
        return amount * 1.25
    # Otherwise return the net income as gross
    return amount
