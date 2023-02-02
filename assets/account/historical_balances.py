from plaid.model.account_assets import AccountAssets

"""
Average Historical Balance
----------------------
avg_historical_balance returns the average daily ending balance in
the given account
"""


def avg_historical_balance(account: AccountAssets) -> int:
    historical_balances = []
    for balance in account.historical_balances:
        historical_balances.append(balance.current)
    return sum(historical_balances) / len(historical_balances)


"""
Minimum Historical Balance
----------------------
min_historical_balance returns the minimum daily ending balance in
the given account
"""


def min_historical_balance(account: AccountAssets) -> float:
    historical_balances = []
    for balance in account.historical_balances:
        historical_balances.append(balance.current)
    return min(historical_balances)


"""
Maximum Historical Balance
----------------------
max_historical_balance returns the maximum daily ending balance across in
the given account
"""


def max_historical_balance(account: AccountAssets) -> float:
    historical_balances = []
    for balance in account.historical_balances:
        historical_balances.append(balance.current)
    return max(historical_balances)
