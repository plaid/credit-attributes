from typing import Dict
from plaid.model.account_assets import AccountAssets
from utils import (
    calculate_user_historical_balances,
    calculate_monthly_summary_of_transactions,
)

"""
Count of inflows
----------------------
num_inflows returns the number of inflow transactions for the user
for a given account
"""


def num_inflows(account: AccountAssets) -> int:
    count = 0
    for transaction in account.transactions:
        if transaction.amount < 0:
            count += 1
    return count


"""
Total inflow amount
----------------------
total_inflows_amount returns the total dollar amount of the users inflows 
for a given account
"""


def total_inflows_amount(account: AccountAssets) -> float:
    total = 0.0
    for transaction in account.transactions:
        if transaction.amount < 0:
            total += transaction.amount
    return total


"""
Inflow Monthly Summary
----------------------
inflows_monthly_summary returns the the total amount of inflows for each
month represented in the account
"""


def inflows_monthly_summary(account: AccountAssets) -> Dict[str, int]:
    inflows = []
    for transaction in account.transactions:
        if transaction.amount < 0:
            inflows.append(transaction)
    return calculate_monthly_summary_of_transactions(inflows)


"""
Count of outflows
----------------------
num_outflows returns the number of inflow transactions for the user
for a given account
"""


def num_outflows(account: AccountAssets) -> int:
    count = 0
    for transaction in account.transactions:
        if transaction.amount > 0:
            count += 1
    return count


"""
Total outflow amount
----------------------
total_outflows_amount returns the total dollar amount of the users outflows 
for a given account
"""


def total_outflows_amount(account: AccountAssets) -> float:
    total = 0.0
    for transaction in account.transactions:
        if transaction.amount > 0:
            total += transaction.amount
    return total


"""
Outflow Monthly Summary
----------------------
outflows_monthly_summary returns the the total amount of outflow for each
month represented in the account
"""


def outflows_monthly_summary(account: AccountAssets) -> Dict[str, int]:
    outflows = []
    for transaction in account.transactions:
        if transaction.amount > 0:
            outflows.append(transaction)
    return calculate_monthly_summary_of_transactions(outflows)


"""
Number of Transactions
----------------------
num_outflows returns the total number of transactions for the user
for a given account
"""


def num_transactions(account: AccountAssets) -> int:
    count = 0
    for transaction in account.transactions:
        count += 1
    return count


"""
Net Cash Flow
----------------------
net_cash_flow returns the total dollar amount of the users cash flow
for a given account
"""


def net_cash_flow(account: AccountAssets) -> float:
    total = 0.0
    for transaction in account.transactions:
        total += transaction.amount
    return total


"""
Monthly Cash Flow
----------------------
monthly_cash_flow returns the the net cash flow for each
month represented in the account
"""


def monthly_cash_flow(account: AccountAssets) -> Dict[str, int]:
    return calculate_monthly_summary_of_transactions(account.transactions)
