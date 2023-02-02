from plaid.model.account_assets import AccountAssets
from typing import Dict
from datetime import datetime
from utils import (
    calculate_user_historical_balances,
    filter_account_transactions_by_category,
    calculate_monthly_summary_of_transactions,
    get_most_recent_transaction,
)

"""
Count of Negative Historical Balances
----------------------
count_negative_historical_balances returns the number of days in which the
user had a negative daily ending balance in the given account
"""


def count_negative_historical_balances(account: AccountAssets) -> int:
    count = 0
    for historical_balance in account.historical_balances:
        if historical_balance.current < 0:
            count += 1
    return count


"""
Lowest Negative Historical Balance
----------------------
lowest_negative_historical_balance returns the lowest negative daily historical
balance held by the user in the given account. If the user doesn't have
a negative balance, then this value will be 0.0
"""


def lowest_negative_historical_balance(account: AccountAssets) -> float:
    min_balance = 0.0
    for balance in account.historical_balances:
        min_balance = min(balance.current, min_balance)
    return min_balance


"""
Average Negative Historical Balance
----------------------
average_negative_historical_balance returns the average negative daily historical
balance held by the user in the given account. If the user doesn't have
any negative balances, then this value will be 0.0
"""


def average_negative_historical_balance(account: AccountAssets) -> float:
    total_negative_historical_balance = 0.0
    num_negative_historical_balance = 0
    for balance in account.historical_balances:
        if balance.current < 0:
            total_negative_historical_balance += balance.current
            num_negative_historical_balance += 1

    if num_negative_historical_balance == 0:
        return 0.0
    return total_negative_historical_balance / num_negative_historical_balance


"""
Count of Overdraft/NSF
----------------------
count_od_nsf returns the number of overdraft or nsf transactions
in the users account
"""


def count_od_nsf(account: AccountAssets) -> int:
    return len(filter_account_transactions_by_category(account, "BANK_PENALTIES"))


"""
Total amount of Overdraft/NSF
----------------------
amount_od_nsf returns the total amount of overdraft or nsf transactions
in the users account
"""


def amount_od_nsf(account: AccountAssets) -> float:
    od_nsf_transactions = filter_account_transactions_by_category(
        account, "BANK_PENALTIES"
    )
    return sum([transaction.amount for transaction in od_nsf_transactions])


"""
Maximum Overdraft/NSF
----------------------
max_od_nsf returns the maximum of overdraft or nsf transactions
in the users account
"""


def max_od_nsf(account: AccountAssets) -> float:
    od_nsf_transactions = filter_account_transactions_by_category(
        account, "BANK_PENALTIES"
    )
    if len(od_nsf_transactions) == 0:
        return 0.0
    return max([transaction.amount for transaction in od_nsf_transactions])


"""
Minimum Overdraft/NSF
----------------------
min_od_nsf returns the maximum of overdraft or nsf transactions
in the users account
"""


def min_od_nsf(account: AccountAssets) -> float:
    od_nsf_transactions = filter_account_transactions_by_category(
        account, "BANK_PENALTIES"
    )
    if len(od_nsf_transactions) == 0:
        return 0.0
    return min([transaction.amount for transaction in od_nsf_transactions])


"""
Average Overdraft/NSF
----------------------
avg_od_nsf returns the average of overdraft or nsf transactions
in the users account
"""


def avg_od_nsf(account: AccountAssets) -> float:
    od_nsf_transactions = filter_account_transactions_by_category(
        account, "BANK_PENALTIES"
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


def od_nsf_monthly_summary(account: AccountAssets) -> Dict[str, float]:
    od_nsf_transactions = filter_account_transactions_by_category(
        account, "BANK_PENALTIES"
    )
    return calculate_monthly_summary_of_transactions(od_nsf_transactions)


"""
Days Since Most Recent OD/NSF
----------------------
days_since_od_nsf returns the number of days since the most recent overdraft or
nsf
"""


def days_since_od_nsf(account: AccountAssets) -> int:
    most_recent_od_nsf = get_most_recent_transaction(
        filter_account_transactions_by_category(account, "BANK_PENALTIES")
    )
    if not most_recent_od_nsf:
        return 0
    return (
        datetime.now() - datetime.strptime(most_recent_od_nsf.date, "%Y-%m-%d")
    ).days
