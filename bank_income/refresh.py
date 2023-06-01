from typing import List
import datetime
from plaid.model.credit_bank_income_get_response import CreditBankIncomeGetResponse
from plaid.model.credit_bank_income_source import CreditBankIncomeSource


"""
get_new_streams takes in a response from /credit/bank_income/get after a refresh and returns
the new income sources that were added to the report after the refresh

Params
* bank_income_get_response: The response from /credit/bank_income/get

Returns
* A list of income sources that were added to the report after the refresh
"""


def get_new_streams(
    bank_income_get_response: CreditBankIncomeGetResponse,
) -> List[CreditBankIncomeSource]:
    original_report = bank_income_get_response.bank_income[1]
    refreshed_report = bank_income_get_response.bank_income[0]

    # Get IDs of income sources in original report
    original_income_source_ids = set()
    for item in original_report.items:
        for source in item.bank_income_sources:
            original_income_source_ids.add(source.income_source_id)

    # Find income sources in refreshed report that are not present in the original report
    new_income_sources = []
    for item in refreshed_report.items:
        for source in item.bank_income_sources:
            if source.income_source_id not in original_income_source_ids:
                new_income_sources.append(source)

    return new_income_sources


"""
get_streams_with_new_transactions takes in a response from /credit/bank_income/get after a refresh and returns
income sources that were updated with new transactions after the refresh

Params
* bank_income_get_response: The response from /credit/bank_income/get

Returns
* A list of income sources that were updated with new transactions after the refresh
"""


def get_streams_with_new_transactions(
    bank_income_get_response: CreditBankIncomeGetResponse,
) -> List[CreditBankIncomeSource]:
    original_report = bank_income_get_response.bank_income[1]
    refreshed_report = bank_income_get_response.bank_income[0]

    # Generate a map of income source to income source end date in the original report
    original_income_source_end_dates = {}
    for item in original_report.items:
        for source in item.bank_income_sources:
            original_income_source_end_dates[source.income_source_id] = source.end_date

    # Find income sources in refreshed report that have been updated with new transactions
    updated_income_sources = []
    for item in refreshed_report.items:
        for source in item.bank_income_sources:
            if source.income_source_id in original_income_source_end_dates:
                if  source.end_date > original_income_source_end_dates[source.income_source_id]:
                    updated_income_sources.append(source)

    return updated_income_sources


def is_source_inactive(
    source: CreditBankIncomeSource, report_generation_time: datetime.datetime
) -> bool:
    source_end_date = datetime.datetime.strptime(source.end_date, "%Y-%m-%d")
    pay_frequency = str(source.pay_frequency)
    time_since_last_transaction = report_generation_time - source_end_date
    if pay_frequency == "WEEKLY":
        if time_since_last_transaction > datetime.timedelta(days=14):
            return True
    elif pay_frequency == "BIWEEKLY" or pay_frequency == "SEMI_MONTHLY":
        if time_since_last_transaction > datetime.timedelta(days=32):
            return True
    else:
        if time_since_last_transaction > datetime.timedelta(days=45):
            return True
    return False


"""
get_inactive_sources takes in a response from /credit/bank_income/get after a refresh and returns
income sources that are no longer active

Params
* bank_income_get_response: The response from /credit/bank_income/get

Returns
* A list of income sources that have become inactive since the previous report generation
"""


def get_inactive_sources(
    bank_income_get_response: CreditBankIncomeGetResponse,
) -> List[CreditBankIncomeSource]:
    refreshed_report = bank_income_get_response.bank_income[0]
    original_report = bank_income_get_response.bank_income[1]

    # Get IDs of inactive sources in original report
    original_inactive_sources_ids = set()
    for item in original_report.items:
        for source in item.bank_income_sources:
            if is_source_inactive(source, original_report.report_generation_time):
                original_inactive_sources_ids.add(source.income_source_id)

    # Find newly inactive sources in refreshed report
    newly_inactive_sources = []
    for item in refreshed_report.items:
        for source in item.bank_income_sources:
            if is_source_inactive(source, refreshed_report.report_generation_time):
                if source.income_source_id not in original_inactive_sources_ids:
                    newly_inactive_sources.append(source)

    return newly_inactive_sources
