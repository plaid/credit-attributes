from plaid.model.asset_report import AssetReport

"""
Number of Outlier Transactions
----------------------
num_outlier_transactions returns the number of transactions across all accounts
that are larger than the outlier_threshold. Default threshold of $10,000.
"""


def num_outlier_transactions(
    asset_report: AssetReport, outlier_threshold: float = 10000.00
) -> int:
    count = 0
    for item in asset_report.items:
        for account in item.accounts:
            for transaction in account.transactions:
                if abs(transaction.amount) > outlier_threshold:
                    count += 1
    return count
