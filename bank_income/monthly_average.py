from typing import List
from datetime import date, timedelta
from plaid.model.credit_bank_income import CreditBankIncome
from plaid.model.credit_bank_income_source import CreditBankIncomeSource
from util import get_total_amount_for_date_range


CATEGORIES_TO_INCLUDE = [
    "SALARY",
    "GIG_ECONOMY",
    "MILITARY",
    "CHILD_SUPPORT",
    "LONG_TERM_DISABILITY",
    "RETIREMENT_PENSION",
    "UNEMPLOYMENT",
    "RENTAL",
    "TAX_REFUND",
]
AVG_DAYS_MONTH = 30.4167


"""
monthly_average_net_income takes in a Bank Income report and estimates the average monthly
net income for that user across their income sources
Params
* report: The Bank Income report to calculate monthly income for.
* active_source_window: The time period, in days, that is used to determine whether an income source is active.
    Only income sources that have recieved a transaction within this number of days will be included in the calculation.
    Default, recommended value is 30 days.
* avg_calculation_window: The time period, in days, over which to calculate the monthly average. We will average over
    a maximum of this many days. Default, recommended value is 90 days.
* categories_to_include: A list of income categories to include in the calculation. Only income sources that fall within one
    of these categories will be considered.

Returns
* An average monthly net income value across the avg_calculation_window
"""


def monthly_average_net_income(
    report: CreditBankIncome,
    active_source_window: int = 30,
    avg_calculation_window: int = 90,
    categories_to_include: List[str] = CATEGORIES_TO_INCLUDE,
) -> float:
    # Get "active" streams. These are defined as streams that have at least one transaction
    # within the active_source_window
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

    # Next, iterate through active sources, calculate average monthly for that source and add it
    # it to the user's total monthly average income
    monthly_average_amount = 0.0
    avg_window_end_date = date.today()
    avg_window_start_date = avg_window_end_date - timedelta(avg_calculation_window)
    for source in active_sources:
        # For tax refund, amortize the amount evenly over the year
        if str(source.income_category) == "TAX_REFUND":
            monthly_average_amount += source.total_amount / 12
            continue

        if source.start_date >= active_window_start_date:
            # For new jobs that started within the active window, average amount over the active window to get a
            # daily average and multiply by the AVG_DAYS_MONTH multiple
            monthly_average_amount += (
                source.total_amount / active_source_window * AVG_DAYS_MONTH
            )
        elif source.start_date >= avg_window_start_date:
            # For jobs that started within the averaging window, average amount since the start date to get a daily average
            # and multiply by the AVG_DAYS_MONTH multiple
            monthly_average_amount += (
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
            monthly_average_amount += (
                amount_in_avg_window / avg_calculation_window * AVG_DAYS_MONTH
            )

    return monthly_average_amount
