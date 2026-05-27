# Plaid Credit Attributes Library

> [!IMPORTANT]
> **This library covers Plaid's legacy credit products — Asset Report and Bank Income.** For most new integrations, these have been superseded by [Plaid Check](https://plaid.com/check/underwriting/) (Plaid's Consumer Reporting Agency / CRA products).
>
> Plaid Check computes many of the attributes in this library directly in the API response, so you generally do not need to run these scripts to derive them. For example, [the Base Report](https://plaid.com/docs/api/products/check/) returns NSF/overdraft transaction counts (`nsf_overdraft_transactions_count`), total inflow/outflow amounts (`total_inflow_amount`, `total_outflow_amount`), and average balances (`average_balance`, `most_recent_thirty_day_average_balance`, `average_monthly_balances`) — with prebuilt 30/60/90-day rolling windows on the cash flow and overdraft fields. Income Insights returns monthly income metrics and `next_payment_date` directly.
>
> **For new underwriting integrations, start with the [Plaid Check Quickstart](https://github.com/plaid/credit-quickstart)** (Base Report, Income Insights, Network Insights, CashFlow Insights, LendScore, Home Lending).
>
> Use this library only if you are maintaining an existing Asset Report or Bank Income integration, or if you need a calculation Plaid Check does not expose directly (for example, loan-disbursement summaries or min/max balance).

Plaid provides a suite of credit products to help lenders gain a holistic view into a user’s finances. Today, these products are used by lenders in verticals across mortgage, personal, and business among others - see the [Credit Underwriting Whitepaper](https://plaid.com/credit-underwriting-whitepaper/) for more details on our product offerings and how Plaid’s Assets and Income improve automation and lending process for our customers today. 

In order to better aid the underwriting process utilizing alternative bank data, we have compiled these attributes on Github for developers and data scientists. This library details how to calculate key attributes from the products that can be used in your underwriting flows across negative records, debt insights, income and more. Each attribute has a corresponding function that you can use or adapt to further understand your user’s finances.

You can find the attributes and documentation for Assets and Bank Income attributes in their respective directories.
