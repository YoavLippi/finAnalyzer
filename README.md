# Yoav Lipshitz 2567169
# Description for Lab Test

This code takes transaction data as a List of transactions and analyses income against expenses to categorize the financial health for the company. 

The five calculations to be done are as follows:
* Total revenue = sum of all income
* Total expenses = sum of all expenses
* Profit = total revenue - total expenses
* Profit margin = profit / revenue
* Average transaction amount = (total revenue - total expenses) / amount of transactions 

The program should then categorize the financial health based on profit according to these rules:
* If profit is Less than -R1000: critical
* Not less than -R1000 but less than R0: warning 
* R0 or over: healthy

The complexity is that this company generates it income from an international market working in Dollars, thus the total profit is require to be converted while the expenses are given in Rand values. We can assume that the exchange rate is measured at a yearly average of $1 = R20. 

The input for this task is an array that contains a list of financial transactions (Date, Type, Amount). A two line example is shown below: the first transaction (2024-01-01) is of type 'income' of $50. The second transaction (2024-01-02) is of type 'expense' of R500.  

```
FinancialTransaction("2024-01-01", "Income", 50),
FinancialTransaction("2024-01-02", "Expense", 500),
```

# How the program should be run

The program is run from the command line as follows:
```
python3 FinancialHealthAnalyzer.py
```

# Expected output

This program should print the profit, profit margin, average transaction amount and financial health of the company to the console for the given transaction data and should then print the test results.
