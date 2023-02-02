from plaid.model.account_assets import AccountAssets
from utils import calculate_user_historical_balances

"""
Number of Outlier Transactions
----------------------
num_outlier_transactions returns the number of transactions in the given account
that are larger than the outlier_threshold. Default threshold of $10,000.
"""


def num_outlier_transactions(
    account: AccountAssets, outlier_threshold: float = 10000.00
) -> int:
    count = 0
    for transaction in account.transactions:
        if abs(transaction.amount) > outlier_threshold:
            count += 1
    return count
