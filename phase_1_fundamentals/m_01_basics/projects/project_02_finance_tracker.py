# ============================================================
# MODULE 01 | PROJECT 02 - Personal Finance Tracker
# ============================================================
# Difficulty  : ⭐⭐⭐⭐ (Hard)
# Covers      : ALL topics from Module 01
#               Variables, Numbers, Strings, Booleans,
#               Print, Input, Comments, Math, Comparisons,
#               Logical operators, Type conversion, F-strings
# Estimated   : 3-5 hours
# ============================================================
#
# OVERVIEW:
# Build a complete personal finance tracker that:
# - Tracks income and expenses
# - Categorizes transactions
# - Calculates statistics
# - Generates formatted reports
# - Validates all input
# - Uses every concept from Module 01
#
# This project has NO biology - it's pure Python applied
# to a real-world everyday use case.
# ============================================================


import math
import datetime


# ============================================================
# SECTION 1: CONFIGURATION AND CONSTANTS
# ============================================================

PROGRAM_NAME    = "Personal Finance Tracker"
VERSION         = "1.0.0"
CURRENCY        = "PLN"
CURRENCY_SYMBOL = "zł"

# Transaction types
TYPE_INCOME  = "income"
TYPE_EXPENSE = "expense"

# Valid categories
INCOME_CATEGORIES = {
    "salary", "freelance", "investment",
    "gift", "bonus", "other_income"
}

EXPENSE_CATEGORIES = {
    "food", "transport", "housing", "entertainment",
    "healthcare", "education", "clothing",
    "utilities", "subscriptions", "other_expense"
}

# Budget thresholds (monthly)
BUDGET_WARNING_THRESHOLD = 0.80    # warn at 80% of budget
BUDGET_CRITICAL_THRESHOLD = 0.95   # critical at 95% of budget

# Tax rate (for income calculations)
INCOME_TAX_RATE = 0.19   # 19% flat tax


# ============================================================
# SECTION 2: SAMPLE TRANSACTION DATA
# ============================================================
# This simulates a month of financial data
# Format: (date, description, amount, type, category)

TRANSACTIONS = [
    # Income
    ("2025-01-01", "Monthly salary",       8500.00, TYPE_INCOME,  "salary"),
    ("2025-01-15", "Freelance Python work", 1200.00, TYPE_INCOME,  "freelance"),
    ("2025-01-20", "Stock dividend",         150.00, TYPE_INCOME,  "investment"),
    ("2025-01-25", "Birthday gift",          200.00, TYPE_INCOME,  "gift"),

    # Fixed expenses
    ("2025-01-01", "Rent",                 2200.00, TYPE_EXPENSE, "housing"),
    ("2025-01-01", "Internet",               89.99, TYPE_EXPENSE, "utilities"),
    ("2025-01-01", "Phone plan",             49.99, TYPE_EXPENSE, "utilities"),
    ("2025-01-01", "Netflix",                49.00, TYPE_EXPENSE, "subscriptions"),
    ("2025-01-01", "Spotify",                23.99, TYPE_EXPENSE, "subscriptions"),
    ("2025-01-01", "Gym membership",         99.00, TYPE_EXPENSE, "healthcare"),

    # Variable expenses - food
    ("2025-01-02", "Grocery shopping",      320.50, TYPE_EXPENSE, "food"),
    ("2025-01-07", "Restaurant dinner",      85.00, TYPE_EXPENSE, "food"),
    ("2025-01-10", "Coffee shop",            42.50, TYPE_EXPENSE, "food"),
    ("2025-01-14", "Grocery shopping",      280.30, TYPE_EXPENSE, "food"),
    ("2025-01-18", "Pizza delivery",         55.00, TYPE_EXPENSE, "food"),
    ("2025-01-21", "Grocery shopping",      195.80, TYPE_EXPENSE, "food"),
    ("2025-01-28", "Grocery shopping",      310.20, TYPE_EXPENSE, "food"),

    # Transport
    ("2025-01-03", "Monthly bus pass",      110.00, TYPE_EXPENSE, "transport"),
    ("2025-01-12", "Uber ride",              35.50, TYPE_EXPENSE, "transport"),
    ("2025-01-19", "Fuel",                  180.00, TYPE_EXPENSE, "transport"),
    ("2025-01-25", "Car parking",            45.00, TYPE_EXPENSE, "transport"),

    # Entertainment
    ("2025-01-06", "Cinema tickets",         60.00, TYPE_EXPENSE, "entertainment"),
    ("2025-01-13", "Video game",             79.99, TYPE_EXPENSE, "entertainment"),
    ("2025-01-20", "Concert tickets",       150.00, TYPE_EXPENSE, "entertainment"),
    ("2025-01-27", "Books",                  89.99, TYPE_EXPENSE, "entertainment"),

    # Healthcare
    ("2025-01-08", "Doctor visit",          150.00, TYPE_EXPENSE, "healthcare"),
    ("2025-01-09", "Pharmacy",               67.50, TYPE_EXPENSE, "healthcare"),

    # Education
    ("2025-01-05", "Online course",         199.00, TYPE_EXPENSE, "education"),
    ("2025-01-15", "Technical book",         59.99, TYPE_EXPENSE, "education"),

    # Clothing
    ("2025-01-11", "Winter jacket",         399.00, TYPE_EXPENSE, "clothing"),
    ("2025-01-22", "Running shoes",         299.00, TYPE_EXPENSE, "clothing"),

    # Other
    ("2025-01-16", "Haircut",               80.00, TYPE_EXPENSE, "other_expense"),
    ("2025-01-24", "Household items",       145.50, TYPE_EXPENSE, "other_expense"),
]

# Monthly budget limits per category
MONTHLY_BUDGETS = {
    "food":          1000.00,
    "transport":      400.00,
    "housing":       2300.00,
    "entertainment":  300.00,
    "healthcare":     300.00,
    "education":      300.00,
    "clothing":       400.00,
    "utilities":      200.00,
    "subscriptions":  150.00,
    "other_expense":  300.00,
}


# ============================================================
# SECTION 3: DISPLAY UTILITIES
# ============================================================
# Tests: f-strings, print(), string formatting


def format_currency(amount, symbol=CURRENCY_SYMBOL, decimals=2):
    """
    Format a number as currency string.

    Args:
        amount  (float): Amount to format.
        symbol  (str)  : Currency symbol.
        decimals(int)  : Decimal places.

    Returns:
        str: Formatted currency string e.g. "1,234.56 zł"
    """
    # YOUR CODE HERE:
    pass


def format_percent(ratio, decimals=1):
    """
    Format a ratio as percentage string.

    Args:
        ratio   (float): Ratio (0.0 to 1.0).
        decimals(int)  : Decimal places.

    Returns:
        str: Formatted percentage e.g. "85.0%"
    """
    # YOUR CODE HERE:
    pass


def make_bar(ratio, width=20, fill="█", empty="░"):
    """
    Create a progress bar for a ratio 0.0-1.0.

    Args:
        ratio (float): Fill ratio (0.0 to 1.0).
        width (int)  : Total bar width.
        fill  (str)  : Fill character.
        empty (str)  : Empty character.

    Returns:
        str: Progress bar string.
    """
    # YOUR CODE HERE:
    pass


def print_header():
    """Print program header banner."""
    # YOUR CODE HERE:
    # Width = 64
    # Show program name, version, current date
    pass


def print_section(title):
    """Print a formatted section header."""
    # YOUR CODE HERE:
    pass


def print_divider(char="─", width=64):
    """Print a divider line."""
    # YOUR CODE HERE:
    pass


# ============================================================
# SECTION 4: TRANSACTION PROCESSING
# ============================================================
# Tests: strings, numbers, type conversion, comparisons


def parse_transaction(transaction_tuple):
    """
    Parse a transaction tuple into a dict.

    Args:
        transaction_tuple (tuple): (date, desc, amount, type, category)

    Returns:
        dict: Parsed transaction with all fields.
    """
    date, description, amount, trans_type, category = transaction_tuple

    # YOUR CODE HERE:
    # Return dict with:
    # date (str), description (str), amount (float),
    # type (str), category (str),
    # is_income (bool), is_expense (bool)
    pass


def get_all_transactions():
    """
    Parse all transactions from TRANSACTIONS list.

    Returns:
        list: List of parsed transaction dicts.
    """
    # YOUR CODE HERE:
    # Use parse_transaction() on each item in TRANSACTIONS
    pass


def filter_by_type(transactions, trans_type):
    """
    Filter transactions by type (income or expense).

    Args:
        transactions (list): List of transaction dicts.
        trans_type   (str) : TYPE_INCOME or TYPE_EXPENSE.

    Returns:
        list: Filtered transactions.
    """
    # YOUR CODE HERE:
    pass


def filter_by_category(transactions, category):
    """
    Filter transactions by category.

    Args:
        transactions (list): List of transaction dicts.
        category     (str) : Category name.

    Returns:
        list: Filtered transactions.
    """
    # YOUR CODE HERE:
    pass


def get_total(transactions):
    """
    Calculate total amount of transactions.

    Args:
        transactions (list): List of transaction dicts.

    Returns:
        float: Sum of all amounts.
    """
    # YOUR CODE HERE:
    pass


def get_category_totals(transactions):
    """
    Calculate total amount per category.

    Args:
        transactions (list): List of transaction dicts.

    Returns:
        dict: {category: total_amount}
    """
    # YOUR CODE HERE:
    pass


# ============================================================
# SECTION 5: FINANCIAL CALCULATIONS
# ============================================================
# Tests: math operators, type conversion, comparisons


def calculate_savings(income_total, expense_total):
    """
    Calculate net savings.

    Args:
        income_total  (float): Total income.
        expense_total (float): Total expenses.

    Returns:
        float: Net savings (can be negative).
    """
    # YOUR CODE HERE:
    pass


def calculate_savings_rate(income_total, expense_total):
    """
    Calculate savings rate as percentage of income.

    Args:
        income_total  (float): Total income.
        expense_total (float): Total expenses.

    Returns:
        float: Savings rate (0.0 to 100.0).
                Returns 0.0 if income is 0.
    """
    # YOUR CODE HERE:
    pass


def calculate_tax(gross_income):
    """
    Calculate income tax using flat rate.

    Args:
        gross_income (float): Gross income before tax.

    Returns:
        tuple: (tax_amount, net_income)
    """
    # YOUR CODE HERE:
    # Use INCOME_TAX_RATE constant
    pass


def calculate_budget_usage(category, spent):
    """
    Calculate budget usage for a category.

    Args:
        category (str)  : Category name.
        spent    (float): Amount spent in category.

    Returns:
        dict: {budget, spent, remaining, ratio, status}
        status: "ok", "warning", or "critical"
    """
    # YOUR CODE HERE:
    # Use MONTHLY_BUDGETS dict
    # Use BUDGET_WARNING_THRESHOLD and BUDGET_CRITICAL_THRESHOLD
    # Return None if category not in MONTHLY_BUDGETS
    pass


def get_largest_expense(transactions):
    """
    Find the single largest expense transaction.

    Args:
        transactions (list): List of all transaction dicts.

    Returns:
        dict: The transaction with highest amount (expenses only).
    """
    # YOUR CODE HERE:
    pass


def get_largest_income(transactions):
    """
    Find the single largest income transaction.

    Args:
        transactions (list): List of all transaction dicts.

    Returns:
        dict: The transaction with highest amount (income only).
    """
    # YOUR CODE HERE:
    pass


def calculate_daily_average(transactions, days=31):
    """
    Calculate average daily spending.

    Args:
        transactions (list): Expense transactions.
        days         (int) : Number of days in period.

    Returns:
        float: Average daily expense.
    """
    # YOUR CODE HERE:
    pass


# ============================================================
# SECTION 6: STATISTICS
# ============================================================
# Tests: math operators, comparisons, type conversion


def calculate_statistics(amounts):
    """
    Calculate descriptive statistics for a list of amounts.

    Args:
        amounts (list): List of float values.

    Returns:
        dict: count, total, mean, min, max, range, median
    """
    if not amounts:
        return {
            "count":  0,
            "total":  0.0,
            "mean":   0.0,
            "min":    0.0,
            "max":    0.0,
            "range":  0.0,
            "median": 0.0,
        }

    # YOUR CODE HERE:
    # count, total, mean, min, max, range
    # median: sort the list, pick middle value
    #   if even count: average of two middle values
    pass


def find_most_expensive_category(category_totals):
    """
    Find the category with highest total spending.

    Args:
        category_totals (dict): {category: total}

    Returns:
        tuple: (category_name, amount)
    """
    # YOUR CODE HERE:
    pass


def find_most_common_category(transactions):
    """
    Find the category with most transactions.

    Args:
        transactions (list): List of expense transactions.

    Returns:
        tuple: (category_name, count)
    """
    # YOUR CODE HERE:
    pass


# ============================================================
# SECTION 7: REPORT GENERATORS
# ============================================================
# Tests: f-strings, print(), ALL formatting


def generate_overview_report(transactions):
    """
    Generate a high-level financial overview report.

    Args:
        transactions (list): All parsed transactions.
    """
    income_txns  = filter_by_type(transactions, TYPE_INCOME)
    expense_txns = filter_by_type(transactions, TYPE_EXPENSE)

    total_income  = get_total(income_txns)
    total_expense = get_total(expense_txns)
    net_savings   = calculate_savings(total_income, total_expense)
    savings_rate  = calculate_savings_rate(total_income, total_expense)
    tax, net      = calculate_tax(total_income)

    print_section("FINANCIAL OVERVIEW - JANUARY 2025")

    # YOUR CODE HERE - print formatted overview:
    #
    # INCOME & EXPENSES
    # Total Income  :  10,050.00 zł
    # Total Expenses:   7,832.75 zł
    # Net Savings   :   2,217.25 zł
    # Savings Rate  :  22.1%
    #
    # TAX CALCULATION
    # Gross Income  :  10,050.00 zł
    # Tax (19%)     :   1,909.50 zł
    # Net Income    :   8,140.50 zł
    #
    # TRANSACTION COUNT
    # Income:    X transactions
    # Expenses:  X transactions
    # Total:     X transactions
    pass


def generate_income_report(transactions):
    """
    Generate detailed income report.

    Args:
        transactions (list): All parsed transactions.
    """
    income_txns = filter_by_type(transactions, TYPE_INCOME)
    category_totals = get_category_totals(income_txns)

    print_section("INCOME REPORT")

    # YOUR CODE HERE - print:
    # By category with amounts and percentages
    # Individual transactions
    # Total at bottom
    #
    # Income by Category:
    # salary         │████████████████████│  8,500.00 zł  84.6%
    # freelance      │████░░░░░░░░░░░░░░░░│  1,200.00 zł  11.9%
    # investment     │░░░░░░░░░░░░░░░░░░░░│    150.00 zł   1.5%
    # gift           │░░░░░░░░░░░░░░░░░░░░│    200.00 zł   2.0%
    pass


def generate_expense_report(transactions):
    """
    Generate detailed expense report with budget tracking.

    Args:
        transactions (list): All parsed transactions.
    """
    expense_txns    = filter_by_type(transactions, TYPE_EXPENSE)
    category_totals = get_category_totals(expense_txns)
    total_expenses  = get_total(expense_txns)

    print_section("EXPENSE REPORT")

    # YOUR CODE HERE - print:
    # By category with budget tracking
    # Status indicators: ✓ OK / ⚠ WARNING / ✗ CRITICAL
    #
    # Category         Spent        Budget       Used     Status
    # ─────────────────────────────────────────────────────────
    # food           1,289.30 zł  1,000.00 zł  128.9%  ✗ OVER
    # transport        370.50 zł    400.00 zł   92.6%  ⚠ HIGH
    # housing        2,200.00 zł  2,300.00 zł   95.7%  ⚠ HIGH
    # ...
    pass


def generate_transaction_list(transactions, title="ALL TRANSACTIONS"):
    """
    Generate a formatted list of transactions.

    Args:
        transactions (list): Transactions to display.
        title        (str) : Section title.
    """
    print_section(title)

    # YOUR CODE HERE - print formatted table:
    #
    # Date        │ Description          │ Category      │  Amount
    # ────────────┼──────────────────────┼───────────────┼──────────
    # 2025-01-01  │ Monthly salary       │ salary        │ +8,500.00
    # 2025-01-01  │ Rent                 │ housing       │ -2,200.00
    # ...
    #
    # Income shown with + prefix
    # Expenses shown with - prefix
    pass


def generate_statistics_report(transactions):
    """
    Generate statistical analysis report.

    Args:
        transactions (list): All parsed transactions.
    """
    expense_txns   = filter_by_type(transactions, TYPE_EXPENSE)
    income_txns    = filter_by_type(transactions, TYPE_INCOME)

    expense_amounts = [t["amount"] for t in expense_txns]
    income_amounts  = [t["amount"] for t in income_txns]

    expense_stats   = calculate_statistics(expense_amounts)
    income_stats    = calculate_statistics(income_amounts)

    print_section("STATISTICAL ANALYSIS")

    # YOUR CODE HERE - print:
    # Expense Statistics:
    #   Count   : X transactions
    #   Total   : X,XXX.XX zł
    #   Mean    : XXX.XX zł
    #   Median  : XXX.XX zł
    #   Minimum : XX.XX zł (description)
    #   Maximum : X,XXX.XX zł (description)
    #   Range   : X,XXX.XX zł
    #
    # Income Statistics: (same format)
    #
    # Daily Averages:
    #   Daily income  : XXX.XX zł
    #   Daily expenses: XXX.XX zł
    #   Daily savings : XXX.XX zł
    pass


def generate_budget_summary(transactions):
    """
    Generate budget compliance summary.

    Args:
        transactions (list): All parsed transactions.
    """
    expense_txns    = filter_by_type(transactions, TYPE_EXPENSE)
    category_totals = get_category_totals(expense_txns)

    print_section("BUDGET SUMMARY")

    # YOUR CODE HERE:
    # Count categories: on_budget, warning, critical, over
    # Print overall budget health score
    # List any over-budget categories
    # Give recommendation
    #
    # Budget Health: 6/10 categories within budget
    # ████████████░░░░░░░░  60.0%
    #
    # ⚠  WARNING CATEGORIES:
    #    transport  : 92.6% of budget used
    #    housing    : 95.7% of budget used
    #
    # ✗  OVER BUDGET:
    #    food       : 128.9% (289.30 zł over)
    #
    # 💡 RECOMMENDATION:
    #    Reduce food spending by ~96.43 zł to meet budget.
    pass


def generate_full_report(transactions):
    """
    Generate the complete financial report.

    Args:
        transactions (list): All parsed transactions.
    """
    print_header()

    generate_overview_report(transactions)
    generate_income_report(transactions)
    generate_expense_report(transactions)
    generate_statistics_report(transactions)
    generate_budget_summary(transactions)
    generate_transaction_list(transactions)

    print(f"\n{'═' * 64}")
    print(f"  Report generated: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"{'═' * 64}\n")


# ============================================================
# SECTION 8: INPUT VALIDATION
# ============================================================
# Tests: input(), type conversion, logical operators, strings


def validate_amount(raw_amount):
    """
    Validate and convert a raw amount string to float.

    Rules:
    - Must be a valid positive number
    - Must be greater than 0
    - Maximum 2 decimal places

    Args:
        raw_amount (str): Raw input string.

    Returns:
        tuple: (is_valid bool, amount float or None, error_msg str)
    """
    # YOUR CODE HERE:
    pass


def validate_category(category, trans_type):
    """
    Validate category for given transaction type.

    Args:
        category   (str): Category to validate.
        trans_type (str): TYPE_INCOME or TYPE_EXPENSE.

    Returns:
        tuple: (is_valid bool, error_msg str)
    """
    # YOUR CODE HERE:
    # Check against INCOME_CATEGORIES or EXPENSE_CATEGORIES
    pass


def validate_date(date_str):
    """
    Validate date string in YYYY-MM-DD format.

    Args:
        date_str (str): Date string to validate.

    Returns:
        tuple: (is_valid bool, error_msg str)
    """
    # YOUR CODE HERE:
    # Check format: YYYY-MM-DD
    # Check reasonable range: 2020-2030
    # Hint: split by "-", check lengths and ranges
    pass


# ============================================================
# SECTION 9: TESTS
# ============================================================


def run_all_tests():
    """Run automated tests for all functions."""
    print_section("RUNNING AUTOMATED TESTS")

    tests_passed = 0
    tests_failed = 0

    def test(description, actual, expected):
        nonlocal tests_passed, tests_failed
        # YOUR CODE HERE:
        # Same as Project 1 test function
        pass

    # Test format_currency():
    test("Format 1234.56",    format_currency(1234.56),    "1,234.56 zł")
    test("Format 0",          format_currency(0),          "0.00 zł")
    test("Format negative",   format_currency(-50.0),      "-50.00 zł")

    # Test format_percent():
    test("50% ratio",         format_percent(0.5),         "50.0%")
    test("100% ratio",        format_percent(1.0),         "100.0%")
    test("0% ratio",          format_percent(0.0),         "0.0%")

    # Test calculate_savings():
    test("Savings 200",       calculate_savings(1000, 800),  200.0)
    test("Savings negative",  calculate_savings(500, 800),  -300.0)

    # Test calculate_savings_rate():
    test("Savings rate 20%",  calculate_savings_rate(1000, 800), 20.0)
    test("Savings rate 0%",   calculate_savings_rate(1000, 1000), 0.0)

    # Test calculate_tax():
    tax, net = calculate_tax(10000)
    test("Tax 1900",          tax,  1900.0)
    test("Net 8100",          net,  8100.0)

    # Test validate_amount():
    valid, amt, _  = validate_amount("100.00")
    test("Valid amount",      valid, True)
    test("Amount 100",        amt,   100.0)

    valid, _, _    = validate_amount("-50")
    test("Negative invalid",  valid, False)

    valid, _, _    = validate_amount("abc")
    test("String invalid",    valid, False)

    # Test get_total():
    parsed = get_all_transactions()
    income = filter_by_type(parsed, TYPE_INCOME)
    total  = get_total(income)
    test("Income > 0",        total > 0, True)

    # Test calculate_statistics():
    stats = calculate_statis12*tics([10, 20, 30, 40, 50])
    test("Count 5",           stats["count"],  5)
    test("Total 150",         stats["total"],  150.0)
    test("Mean 30",           stats["mean"],   30.0)
    test("Min 10",            stats["min"],    10.0)
    test("Max 50",            stats["max"],    50.0)
    test("Median 30",         stats["median"], 30.0)

    # Print summary:
    total_tests = tests_passed + tests_failed
    print(f"\n  Results: {tests_passed}/{total_tests} tests passed")
    if tests_failed == 0:
        print("  ✓ All tests passed!")
    else:
        print(f"  ✗ {tests_failed} test(s) failed")


# ============================================================
# MAIN PROGRAM
# ============================================================


def main():
    """Main program entry point."""
    # Parse all transactions:
    transactions = get_all_transactions()

    # Run tests first:
    run_all_tests()

    # Generate complete report:
    generate_full_report(transactions)


if __name__ == "__main__":
    main()

# ============================================================
# END OF PROJECT 02
# ============================================================