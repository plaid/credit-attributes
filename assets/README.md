# Asset Report Attributes

The [Plaid Asset Report](https://plaid.com/products/assets/) contains a holistic view into a user’s finances, including their transactions, balances, and historical cash flows in their financial accounts. Today, Assets is used by lenders in all verticals across mortgage, personal, and business among others - see the [Credit Underwriting Whitepaper](https://plaid.com/credit-underwriting-whitepaper/) for more details on our product offerings and how Plaid’s Assets and Income improve automation and lending process for our customers today. 

In order to better aid the underwriting process utilizing alternative bank data, we have compiled these attributes on Github for developers and data scientists. This library details how to calculate key attributes from the report that can be used in your underwriting flows across negative records, debt insights, unusual account activity, cash flow and historical balances. Each attribute has a corresponding function that you can use or adapt to further understand your user’s finances. Please note in order to use these attributes, you will need credit categories enabled. 

Please reach out to your account manager if you have further questions on how to utilize the report attributes or have the credit categories from Assets enabled. 

## Table of Contents
1. [Negative Records](#Negative-Records)
    - [Count of OD/NSF events](#count-of-od/nsf-events)
    - [Total amount of OD/NSF events](#total-amount-of-od/nsf-events)
    - [Monthly Summary of OD/NSF events](#monthly-summary-of-od/nsf-events)
    - [Minimum of OD/NSF events](#minimum-of-od/nsf-events)
    - [Maximum of OD/NSF events](#maximum-of-od/nsf-events)
    - [Average of OD/NSF events](#average-of-od/nsf-events)
    - [Days Since most recent OD/NSF event](#days-since-most-recent-od/nsf-event)
    - [Count of Negative Historical Balances](#count-of-negative-historical-balances)
    - [Total amount of Negative Historical Balances](#total-amount-of-negative-historical-balances)
    - [Average of Negative Historical Balances](#average-of-negative-historical-balances)
    - [Days since most recent Negative Historical Balance](#days-since-most-recent-negative-historical-balance)
2. [Debt Insights](#Debt-Insights)
    - [Count of Loan Disbursements](#count-of-loan-disbursements) / [Payments](#count-of-loan-payments)
    - [Total amount of Loan Disbursements](#total-amount-of-loan-payments) / [Payments](#total-amount-of-loan-payments)
    - [Monthly Summary of Loan Disbursements](#monthly-summary-of-loan-disbursements) / [Payments](#monthly-summary-of-loan-payments)
    - [Minimum of Loan Disbursements](#minimum-of-loan-disbursements) / [Payments](#minimum-of-loan-payments)
    - [Maximum of Loan Disbursements](#maximum-of-loan-disbursements) / [Payments](#maximum-of-loan-payments)
    - [Average of Loan Disbursements](#average-of-loan-disbursements) / [Payments](#average-of-loan-payments)
    - [Days Since most recent Loan Disbursement](#days-since-most-recent-loan-disbursement) / [Payments](#days-since-most-recent-loan-payment)
3. [Unusual Account Activity](#Unusual-Account-Activity)
    - [Outlier Event](#outlier-event)
4. [Cash Flow](#Cash-Flow)
    - [Count of Inflows](#count-of-inflows) / [Outflows](#count-of-outflows)
    - [Total Amount of Inflows](#total-amount-of-inflows) / [Outflows](#total-amount-of-outflows)
    - [Count of Transactions](#count-of-transactions)
    - [Net Cash Flow](#net-cash-flow)
4. [Historical Balances](#Historical-Balances)
    - [Average of Historical Balances](#average-of-historical-balances)
    - [Minimum Historical Balances](#minimum-historical-balances)
    - [Maximum Historical Balances](#maximum-historical-balances)

## Negative Records
### Count of OD/NSF events
This attribute details how many times the user has received overdraft and NSF fees in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Total amount of OD/NSF events
This attribute details the total amount of overdraft and NSF fees the user has received in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Monthly Summary of OD/NSF events
This attribute details a monthly summary of overdraft and NSF fees for the user. The output will include the total fees for each month in the report

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Minimum of OD/NSF events
This attribute details the minimum overdraft or NSF fee for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Maximum of OD/NSF events
This attribute details the maximum overdraft or NSF fee for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Average of OD/NSF events
This attribute details the average of all overdraft or NSF fees for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Days Since most recent OD/NSF event
This attribute outputs the number of days since the most recent overdraft or NSF for the user

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Count of Negative Historical Balances
This attribute details how many times the user has ended the day with a negative balance.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Total amount of Negative Historical Balances
This attribute details the total amount of negative daily ending balances the user has accrued.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Average of Negative Historical Balances
This attribute details the average of a user’s negative daily ending balances(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Days since most recent Negative Historical Balance
This attribute details the number of days since the most recent negative daily ending balance

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

## Debt Insights
### Count of Loan Disbursements
This attribute details how many times the user has received a loan disbursement in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Total amount of Loan Disbursements
This attribute details the total amount of loan disbursements the user has received in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Monthly Summary of Loan Disbursements
This attribute details a monthly summary of loan disbursements for the user. The output will include the total disbursements for each month in the report

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Minimum of Loan Disbursements
This attribute details the minimum loan disbursement for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Maximum of Loan Disbursements
This attribute details the maximum loan disbursement for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Average of Loan Disbursements
This attribute details the average of all loan disbursements for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Days Since most recent Loan Disbursement
This attribute outputs the number of days since the most recent loan disbursement for the user

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Count of Loan Payments
This attribute details how many times the user has paid a loan payment in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Total amount of Loan Payments
This attribute details the total amount of loan payments the user has has paid in the time range for the report.

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Monthly Summary of Loan Payments
This attribute details a monthly summary of loan payments for the user. The output will include the total amount for each month in the report

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Minimum of Loan Payments
This attribute details the minimum loan payment for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Maximum of Loan Payments
This attribute details the maximum loan payment for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Average of Loan Payments
This attribute details the average of all loan payments for the user(if applicable).

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

### Days Since most recent Loan Payment
This attribute outputs the number of days since the most recent loan payment for the user

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/debt_insights.py
* Report level attribute: report/debt_insights.py

## Unusual Account Activity
### Outlier Event
This attribute outputs the number of outlier transactions for the user, defined as having an absolute value greater than 10,000

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/unusual_account_activity.py
* Report level attribute: report/unusual_account_activity.py

# Cash Flow
### Count of Inflows
This attribute details the number of inflow transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Total amount of Inflows
This attribute details the sum amount of inflow transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Monthly summary of Inflows
This attribute details the total amount of inflows for the user, broken down by each
month represented in the report

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Count of Outflows
This attribute details the number of outflow transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Total amount of Outflows
This attribute details the sum amount of outflow transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Monthly summary of Outflows
This attribute details the total amount of outflows for the user, broken down by each
month represented in the report

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Count of Transactions
This attribute details the number of transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Net Cash Flow
This attribute details the net cash flow for the user, or in other words, the sum amount of transactions for the user

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

### Monthly summary of Cash Flow
This attribute details the total net cash flow for the user, broken down by each
month represented in the report

This attribute can be calculated for a single account or across all the users accounts.
* Account level attribute: account/cash_flow.py
* Report level attribute: report/cash_flow.py

## Historical Balances
### Average of Historical Balances
This attribute details the average of a user’s daily ending balances

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Minimum Historical Balances
This attribute details the minimum daily ending balance for a user

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py

### Maximum Historical Balances
This attribute details the maximum daily ending balance for a user

This attribute can be calculated for a single account or across all the users depository accounts.
* Account level attribute: account/negative_record.py
* Report level attribute: report/negative_record.py
