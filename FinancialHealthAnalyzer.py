import unittest
from io import StringIO

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income"
    #Converts from $1 to R20
    def total_revenue(self):
        #using list comprehension here to iterate through all transactions
        return sum(transaction.amount*20 for transaction in self.transactions if transaction.type == "Income")

    #Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")

    #Subtracts total expenses from total revenue and returns the result
    def profit(self):
        return self.total_revenue() - self.total_expenses() 

    #Returns revenue-expenses (profit) divided by gross revenue
    def profit_margin(self):
        return self.profit() / self.total_revenue()
    
    #Returns profit divided by number of transactions (the size of the tuple containing transactions)
    def average_transaction_amount(self):
        return self.profit() / len(self.transactions)

    #Determines finalncial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        # using interval comparison to check if within range
        elif -1000 <= profit < 0:
            return "Warning"
        else:
            return "Critical"

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 1500)
        ]
        self.transactions = transactions_data

    def set_health_to_warning(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Expense", 500)
        ]
        self.transactions = transactions_data

    def set_health_to_critical(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Expense", 1200)
        ]
        self.transactions = transactions_data

    #helper method to set up analyzer
    def create_analyzer(self):
        return FinancialHealthAnalyzer(self.transactions)

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    #Rewritten to use AAA unit testing pattern

    def test_total_revenue(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = 50000

        #Act
        actual = analyzer.total_revenue()

        #Assert
        self.assertEqual(actual, expected)

    def test_total_expenses(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = 800

        #Act
        actual = analyzer.total_expenses()

        #Assert
        self.assertEqual(actual, expected)

    def test_profit(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = 49200

        #Act
        actual = analyzer.profit()

        #Assert
        self.assertEqual(actual, expected)

    def test_profit_margin(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = 0.984

        #Act
        actual = analyzer.profit_margin()

        #Assert
        self.assertEqual(actual, expected)
    
    def test_average_transaction_amount(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = 12300

        #Act
        actual = analyzer.average_transaction_amount()

        #Assert
        self.assertEqual(actual, expected)

    def test_financial_health_if_warning(self):
        #Arrange
        self.set_health_to_warning()
        analyzer = self.create_analyzer()
        expected = "Warning"

        #Act
        actual = analyzer.financial_health()

        #Assert
        self.assertEqual(actual, expected)

    def test_financial_health_if_critical(self):
        #Arrange
        self.set_health_to_critical()
        analyzer = self.create_analyzer()
        expected = "Critical"

        #Act
        actual = analyzer.financial_health()

        #Assert
        self.assertEqual(actual, expected)

    def test_financial_health_if_healthy(self):
        #Arrange
        analyzer = self.create_analyzer()
        expected = "Healthy"

        #Act
        actual = analyzer.financial_health()

        #Assert
        self.assertEqual(actual, expected)

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    #changed outputs to f-strings for easier formatting
    print(f"Profit: {analyzer.profit()}")
    print(f"Profit margin: {analyzer.profit_margin()}")
    print(f"Average transaction amount: {analyzer.average_transaction_amount()}")
    print(f"Financial health: {analyzer.financial_health()}")
    unittest.main()
