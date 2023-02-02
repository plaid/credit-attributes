from plaid.model.asset_report import AssetReport
from attributes.utils import (
    calculate_user_historical_balances,
)

"""
Average Historical Balance
----------------------
avg_historical_balance returns the average daily ending balance across all
accounts in the report
"""


def avg_historical_balance(asset_report: AssetReport) -> int:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    return sum(user_historical_balances.values()) / len(user_historical_balances)


"""
Minimum Historical Balance
----------------------
min_historical_balance returns the minimum daily ending balance across all
accounts in the report
"""


def min_historical_balance(asset_report: AssetReport) -> float:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    return min(user_historical_balances.values())


"""
Maximum Historical Balance
----------------------
max_historical_balance returns the maximum daily ending balance across all
accounts in the report
"""


def max_historical_balance(asset_report: AssetReport) -> float:
    user_historical_balances = calculate_user_historical_balances(asset_report, True)
    return max(user_historical_balances.values())
