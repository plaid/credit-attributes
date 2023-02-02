from typing import Dict, List
from collections import defaultdict
from datetime import datetime


from plaid.model.asset_report import AssetReport
from plaid.model.asset_report_transaction import AssetReportTransaction
from plaid.model.account_assets import AccountAssets


"""
calculate_user_historical_balances takes in an asset report and returns the net historical 
balances aggregated across all accounts for the user.

Params
* asset_report: the asset report retrieved through /asset_report/get
* include_depository_account: whether to ignore all non-depository accounts

Returns
* A map of date to the users net balance across all accounts on that date 
"""


def calculate_user_historical_balances(
    asset_report: AssetReport,
    include_depository_only: bool = False,
) -> Dict[str, float]:
    user_historical_balances = defaultdict(float)
    for item in asset_report.items:
        for account in item.accounts:
            if include_depository_only and str(account.type) != "depository":
                continue
            for balance in account.historical_balances:
                user_historical_balances[balance.date] += balance.current
    return user_historical_balances


"""
filter_account_transactions_by_category takes in an asset account and returns the
transactions in the account that match a given category

Params
* asset_report_account: one of the accounts retrieved through /asset_report/get
* primary_category: the primary category for which the transactions should be filtered
* secondary_category: the (optional) secondary category for which the transactions should be filtered

Returns
* A list of transactions that match the given category
"""


def filter_account_transactions_by_category(
    asset_report_account: AccountAssets,
    primary_category: str,
    detailed_category: str = "",
) -> List[AssetReportTransaction]:
    filtered_transactions = []
    for transaction in asset_report_account.transactions:
        if transaction.credit_category.primary != primary_category:
            continue
        if (
            detailed_category
            and transaction.credit_category.detailed != detailed_category
        ):
            continue
        filtered_transactions.append(transaction)
    return filtered_transactions


"""
filter_account_transactions_by_category takes in an asset report and returns the
transactions in the report that match a given category

Params
* asset_report: the asset report retrieved through /asset_report/get
* primary_category: the primary category for which the transactions should be filtered
* secondary_category: the (optional) secondary category for which the transactions should be filtered
* include_depository_only: whether to exclude transactions from non depository accounts

Returns
* A list of transactions that match the given category
"""


def filter_report_transactions_by_category(
    report: AssetReport,
    primary_category: str,
    detailed_category: str = "",
    include_depository_only: bool = False,
) -> List[AssetReportTransaction]:
    filtered_transactions = []
    for item in report.items:
        for account in item.accounts:
            if include_depository_only and str(account.type) != "depository":
                continue
            filtered_transactions.extend(
                filter_account_transactions_by_category(
                    account, primary_category, detailed_category
                )
            )
    return filtered_transactions


"""
calculate_monthly_summary_of_transactions takes in a list of transactions and returns a map
of month to the net amount of the transactions for the month

Params
* transactions: a list of transactions

Returns
* A map of month to the net amount for that month
"""


def calculate_monthly_summary_of_transactions(
    transactions: List[AssetReportTransaction],
) -> Dict[str, float]:
    monthly_summary = defaultdict(float)
    for transaction in transactions:
        monthly_summary[transaction.date.strftime("%Y-%m")] += transaction.amount
    return monthly_summary


"""
get_most_recent_transaction takes in a list of transactions and returns the
most recent transaction from that list

Params
* transactions: a list of transactions

Returns
* The most recent transaction from the input
"""


def get_most_recent_transaction(
    transactions: List[AssetReportTransaction],
) -> AssetReportTransaction:
    if len(transactions) == 0:
        return None
    return max(
        transactions,
        key=lambda transaction: transaction.date,
    )
