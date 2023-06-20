from typing import Optional
from datetime import date, timedelta
from plaid.model.credit_bank_income_source import CreditBankIncomeSource


# The expected days between pay for a given pay frequency
EXPECTED_CADENCE = {"WEEKLY": 7, "BIWEEKLY": 14, "MONTHLY": 30, "SEMI_MONTHLY": 15}

# The allowed buffer/error allowed for a given pay frequency
BUFFER = {"WEEKLY": 1, "BIWEEKLY": 2, "MONTHLY": 3, "SEMI_MONTHLY": 4}

"""
next_expected_pay_date takes in a Bank Income Source and predicts the next pay date
for that source
Params
* source: The Bank Income source to predict the next pay date for.

Returns
* The next expected pay date for the source. If we are unable to predict the next pay date,
    None will be returned.
"""


def next_expected_pay_date(source: CreditBankIncomeSource) -> Optional[date]:
    # If the source doesn't have a known frequency, then we are unable to predict
    # the next pay date
    if str(source.pay_frequency) == "UNKNOWN":
        return None

    frequency = str(source.pay_frequency)
    days_since_pay = date.today() - source.end_date

    if days_since_pay.days < EXPECTED_CADENCE[frequency]:
        # If it hasn't been the expected amount of days since the last
        # pay date, simply add the expected amount of days for the frequency
        return source.end_date + timedelta(EXPECTED_CADENCE[frequency])
    elif days_since_pay.days <= EXPECTED_CADENCE[frequency] + BUFFER[frequency]:
        # If the expected number of days has already passed, but within the buffer/error
        # window for the frequency, return tommorrow's date
        return date.today() + 1
    elif days_since_pay.days < EXPECTED_CADENCE[frequency] * 2:
        # Otherwise assume that the subsequent pay date has been missed and return
        # the one after that
        return source.end_date + timedelta(EXPECTED_CADENCE[frequency] * 2)
    # If none of the above conditions apply then assume the income source has ended
    return None
