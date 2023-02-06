# Bank Income Attributes

The [Plaid Bank Income](https://plaid.com/products/income/) product helps verify a user's income using bank data, including income from payroll, government income, and other sources. This library details how to calculate key attributes from the Bank Income data that can be used in your verification flows. Each attribute has a corresponding function that you can use or adapt to further understand your user’s finances.

Please reach out to your account manager if you have further questions on how to utilize the attributes.

### Monthly Average Income(Net and Gross)
These attributes details how to estimate a user’s average monthly net income across all of their income sources and how to estimate the monthly gross income for that user from their net income. You can configure what time period you want to average over and what categories to include in the calculation.

These attributes can be found in monthly_average.py

### Next Pay Date
This attribute gives a prediction of the next pay date for a given income source.

The attribute can be found in next_pay_date.py
