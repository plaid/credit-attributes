from plaid.model.asset_report import AssetReport
from datetime import date
from typing import Dict
from utils import (
    calculate_user_historical_balances,
    filter_report_transactions_by_category,
    calculate_monthly_summary_of_transactions,
    get_most_recent_transaction,
)

"""
Count of Negative Historical Balances
----------------------
count_negative_historical_balances returns the number of days in which the
user had a negative daily ending balance across all their accounts
"""


def count_negative_historical_balances(asset_report: AssetReport) -> int:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    count = 0
    for date, balance in user_historical_balances.items():
        if balance < 0:
            count += 1
    return count


"""
Lowest Negative Historical Balance
----------------------
lowest_negative_historical_balance returns the lowest negative daily historical
balance held by the user across all accounts in the report. If the user doesn't have
a negative balance, then this value will be 0.0
"""


def lowest_negative_historical_balance(asset_report: AssetReport) -> float:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    min_balance = 0.0
    for balance in user_historical_balances.values():
        min_balance = min(balance, min_balance)
    return min_balance


"""
Average Negative Historical Balance
----------------------
average_negative_historical_balance returns the average negative daily historical
balance held by the user across all accounts in the report. If the user doesn't have
any negative balances, then this value will be 0.0
"""


def average_negative_historical_balance(asset_report: AssetReport) -> float:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    total_negative_historical_balance = 0.0
    num_negative_historical_balance = 0
    for balance in user_historical_balances.values():
        if balance < 0:
            total_negative_historical_balance += balance
            num_negative_historical_balance += 1

    if num_negative_historical_balance == 0:
        return 0.0
    return total_negative_historical_balance / num_negative_historical_balance


"""
Count of Overdraft/NSF
----------------------
count_od_nsf returns the number of overdraft or nsf transactions
across the users accounts
"""


def count_od_nsf(asset_report: AssetReport) -> int:
    return len(filter_report_transactions_by_category(asset_report, []))


"""
Total amount of Overdraft/NSF
----------------------
amount_od_nsf returns the total number of overdraft or nsf transactions
across the users accounts
"""


def amount_od_nsf(asset_report: AssetReport) -> float:
    od_nsf_transactions = filter_report_transactions_by_category(
        asset_report, "BANK_PENALTIES", include_depository_only=True
    )
    return sum([transaction.amount for transaction in od_nsf_transactions])


"""
Maximum Overdraft/NSF
----------------------
max_od_nsf returns the maximum of overdraft or nsf transactions
across the users accounts
"""


def max_od_nsf(asset_report: AssetReport) -> float:
    od_nsf_transactions = filter_report_transactions_by_category(
        asset_report, "BANK_PENALTIES", include_depository_only=True
    )
    if len(od_nsf_transactions) == 0:
        return 0.0
    return max([transaction.amount for transaction in od_nsf_transactions])


"""
Minimum Overdraft/NSF
----------------------
min_od_nsf returns the maximum of overdraft or nsf transactions
across the users accounts
"""


def min_od_nsf(asset_report: AssetReport) -> float:
    od_nsf_transactions = filter_report_transactions_by_category(
        asset_report, "BANK_PENALTIES", include_depository_only=True
    )
    if len(od_nsf_transactions) == 0:
        return 0.0
    return min([transaction.amount for transaction in od_nsf_transactions])


"""
Average Overdraft/NSF
----------------------
avg_od_nsf returns the average of overdraft or nsf transactions
across the users accounts
"""


def avg_od_nsf(asset_report: AssetReport) -> float:
    od_nsf_transactions = filter_report_transactions_by_category(
        asset_report, "BANK_PENALTIES", include_depository_only=True
    )
    if len(od_nsf_transactions) == 0:
        return 0.0
    return sum([transaction.amount for transaction in od_nsf_transactions]) / len(
        od_nsf_transactions
    )


"""
OD/NSF Monthly Summary
----------------------
od_nsf_monthly_summary returns the the total amount of overdraft or nsf transactions for each
month represented in the report
"""


def od_nsf_monthly_summary(asset_report: AssetReport) -> Dict[str, float]:
    od_nsf_transactions = filter_report_transactions_by_category(
        asset_report, "BANK_PENALTIES", include_depository_only=True
    )
    return calculate_monthly_summary_of_transactions(od_nsf_transactions)


"""
Days Since Most Recent OD/NSF
----------------------
days_since_od_nsf returns the number of days since the most recent overdraft or
nsf
"""


def days_since_od_nsf(asset_report: AssetReport) -> int:
    most_recent_od_nsf = get_most_recent_transaction(
        filter_report_transactions_by_category(
            asset_report, "BANK_PENALTIES", include_depository_only=True
        )
    )
    if not most_recent_od_nsf:
        return 0
    return (date.today() - most_recent_od_nsf.date).days
