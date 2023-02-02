from typing import Dict
from plaid.model.asset_report import AssetReport
from utils import calculate_monthly_summary_of_transactions

"""
Count of inflows
----------------------
num_inflows returns the number of inflow transactions for the user
across all accounts
"""


def num_inflows(asset_report: AssetReport) -> int:
    count = 0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount < 0:
                    count += 1
    return count


"""
Total inflow amount
----------------------
total_inflows_amount returns the total dollar amount of the users inflows 
across all their account.
"""


def total_inflows_amount(asset_report: AssetReport) -> float:
    total = 0.0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount < 0:
                    total += transaction.amount
    return total


"""
Inflow Monthly Summary
----------------------
inflows_monthly_summary returns the the total amount of inflows for each
month represented in the report
"""


def inflows_monthly_summary(asset_report: AssetReport) -> Dict[str, int]:
    inflows = []
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount < 0:
                    inflows.append(transaction)
    return calculate_monthly_summary_of_transactions(inflows)


"""
Count of outflows
----------------------
num_outflows returns the number of inflow transactions for the user
across all accounts
"""


def num_outflows(asset_report: AssetReport) -> int:
    count = 0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount > 0:
                    count += 1
    return count


"""
Total outflow amount
----------------------
total_outflows_amount returns the total dollar amount of the users outflows 
across all their account.
"""


def total_outflows_amount(asset_report: AssetReport) -> float:
    total = 0.0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount > 0:
                    total += transaction.amount
    return total


"""
Outflow Monthly Summary
----------------------
outflows_monthly_summary returns the the total amount of outflows for each
month represented in the report
"""


def outflows_monthly_summary(asset_report: AssetReport) -> Dict[str, int]:
    outflows = []
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if transaction.amount > 0:
                    outflows.append(transaction)
    return calculate_monthly_summary_of_transactions(outflows)


"""
Number of Transactions
----------------------
num_outflows returns the total number of transactions for the user
across all accounts
"""


def num_transactions(asset_report: AssetReport) -> int:
    count = 0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                count += 1
    return count


"""
Net Cash Flow
----------------------
net_cash_flow returns the total dollar amount of the users cash flow
across all accounts
"""


def net_cash_flow(asset_report: AssetReport) -> float:
    total = 0.0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                total += transaction.amount
    return total


"""
Monthly Cash Flow
----------------------
monthly_cash_flow returns the the net cash flow for each
month represented in the report
"""


def cash_flow_monthly_summary(asset_report: AssetReport) -> Dict[str, int]:
    transactions = []
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                transactions.append(transaction)
    return calculate_monthly_summary_of_transactions(transactions)
