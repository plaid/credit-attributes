from typing import Dict
from plaid.model.asset_report import AssetReport
from datetime import date
from utils import (
    calculate_user_historical_balances,
    filter_report_transactions_by_category,
    calculate_monthly_summary_of_transactions,
    get_most_recent_transaction,
)

"""
Count of Loan Disburstments
----------------------
count_loan_disbursements returns the number of loan disbursement transactions
across the users accounts
"""


def count_loan_disbursements(asset_report: AssetReport) -> int:
    return len(
        filter_report_transactions_by_category(
            asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
        )
    )


"""
Total amount of Loan Disburstments
----------------------
amount_loan_disbursements returns the total amount of loan disbursement transactions
across the users accounts
"""


def amount_loan_disbursements(asset_report: AssetReport) -> float:
    loan_disbursement_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
    )
    return sum([transaction.amount for transaction in loan_disbursement_transactions])


"""
Maximum Loan Disburstments
----------------------
max_loan_disbursements returns the maximum of loan disbursement transactions
across the users accounts
"""


def max_loan_disbursements(asset_report: AssetReport) -> float:
    loan_disbursement_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
    )
    if len(loan_disbursement_transactions) == 0:
        return 0.0
    return max([transaction.amount for transaction in loan_disbursement_transactions])


"""
Minimum Loan Disburstments
----------------------
min_loan_disbursements returns the minimum of loan disbursement transactions
across the users accounts
"""


def min_loan_disbursements(asset_report: AssetReport) -> float:
    loan_disbursement_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
    )
    if len(loan_disbursement_transactions) == 0:
        return 0.0
    return min([transaction.amount for transaction in loan_disbursement_transactions])


"""
Average Loan Disbursement
----------------------
avg_loan_disbursement returns the average of loan disbursement transactions
across the users accounts
"""


def avg_loan_disbursement(asset_report: AssetReport) -> float:
    loan_disbursement_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
    )
    if len(loan_disbursement_transactions) == 0:
        return 0.0
    return sum(
        [transaction.amount for transaction in loan_disbursement_transactions]
    ) / len(loan_disbursement_transactions)


"""
Loan Disbursement Monthly Summary
----------------------
loan_disbursement_monthly_summary returns the the total amount of loan disbursements for each
month represented in the report
"""


def loan_disbursement_monthly_summary(asset_report: AssetReport) -> Dict[str, float]:
    loan_disbursement_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
    )
    return calculate_monthly_summary_of_transactions(loan_disbursement_transactions)


"""
Days Since Most Recent Loan Disbursement
----------------------
days_since_loan_disbursement returns the number of days since the most recent
loan disbursement
"""


def days_since_loan_disbursement(asset_report: AssetReport) -> int:
    most_recent_loan_disbursement = get_most_recent_transaction(
        filter_report_transactions_by_category(
            asset_report, "LOAN_DISBURSEMENTS", include_depository_only=True
        )
    )
    if not most_recent_loan_disbursement:
        return 0
    return (date.today() - most_recent_loan_disbursement.date).days


"""
Count of Loan Payments
----------------------
count_loan_payments returns the number of loan payment transactions
across the users accounts
"""


def count_loan_payments(asset_report: AssetReport) -> int:
    return len(filter_report_transactions_by_category(asset_report, "LOAN_PAYMENTS"))


"""
Total amount of Loan Payments
----------------------
amount_loan_payments returns the total amount of loan payment transactions
across the users accounts
"""


def amount_loan_payments(asset_report: AssetReport) -> float:
    loan_payment_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_PAYMENTS"
    )
    return sum([transaction.amount for transaction in loan_payment_transactions])


"""
Maximum Loan Payments
----------------------
max_loan_payments returns the maximum of loan payment transactions
across the users accounts
"""


def max_loan_payments(asset_report: AssetReport) -> float:
    loan_payment_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_PAYMENTS"
    )
    if len(loan_payment_transactions) == 0:
        return 0.0
    return max([transaction.amount for transaction in loan_payment_transactions])


"""
Minimum Loan Payments
----------------------
min_loan_payments returns the minimum of loan payment transactions
across the users accounts
"""


def min_loan_payments(asset_report: AssetReport) -> float:
    loan_payment_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_PAYMENTS"
    )
    if len(loan_payment_transactions) == 0:
        return 0.0
    return min([transaction.amount for transaction in loan_payment_transactions])


"""
Average Loan payment
----------------------
avg_loan_payment returns the average of loan payment transactions
across the users accounts
"""


def avg_loan_payment(asset_report: AssetReport) -> float:
    loan_payment_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_PAYMENTS"
    )
    if len(loan_payment_transactions) == 0:
        return 0.0
    return sum([transaction.amount for transaction in loan_payment_transactions]) / len(
        loan_payment_transactions
    )


"""
Loan Payment Monthly Summary
----------------------
loan_payment_monthly_summary returns the the total amount of loan payments for each
month represented in the report
"""


def loan_payment_monthly_summary(asset_report: AssetReport) -> Dict[str, float]:
    loan_payment_transactions = filter_report_transactions_by_category(
        asset_report, "LOAN_PAYMENTS"
    )
    return calculate_monthly_summary_of_transactions(loan_payment_transactions)


"""
Days Since Most Recent Loan Payment
----------------------
days_since_loan_payment returns the number of days since the most recent
loan_payment
"""


def days_since_loan_payment(asset_report: AssetReport) -> int:
    most_recent_loan_payment = get_most_recent_transaction(
        filter_report_transactions_by_category(asset_report, "LOAN_PAYMENTS")
    )
    if not most_recent_loan_payment:
        return 0
    return (date.today() - most_recent_loan_payment.date).days
