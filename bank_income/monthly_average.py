from typing import List
from datetime import date, timedelta
from plaid.model.credit_bank_income import CreditBankIncome
from plaid.model.credit_bank_income_source import CreditBankIncomeSource
from util import (
    get_active_sources,
    get_total_amount_for_date_range,
    source_monthly_avg_net_income,
    get_gross_income_from_net_income,
)


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
    active_sources = get_active_sources(
        report, active_source_window, categories_to_include
    )

    # Next, iterate through active sources, calculate average monthly for that source and add it
    # it to the user's total monthly average income
    net_monthly_average = 0.0
    for source in active_sources:
        net_monthly_average += source_monthly_avg_net_income(
            source, active_source_window, avg_calculation_window
        )
    return net_monthly_average


"""
monthly_average_gross_income takes in a Bank Income report and estimates the average monthly
gross income for that user across their income sources
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
* An average monthly gross income value across the avg_calculation_window
"""


def monthly_average_gross_income(
    report: CreditBankIncome,
    active_source_window: int = 30,
    avg_calculation_window: int = 90,
    categories_to_include: List[str] = CATEGORIES_TO_INCLUDE,
) -> float:
    # Get "active" streams. These are defined as streams that have at least one transaction
    # within the active_source_window
    active_sources = get_active_sources(
        report, active_source_window, categories_to_include
    )

    # Next, iterate through active sources, calculate average gross monthly for that source and add it
    # it to the user's total monthly average gross income
    gross_monthly_average = 0.0
    for source in active_sources:
        monthly_average_net_amount = source_monthly_avg_net_income(
            source, active_source_window, avg_calculation_window
        )
        gross_monthly_average += get_gross_income_from_net_income(
            monthly_average_net_amount, str(source.income_category)
        )
    return gross_monthly_average
